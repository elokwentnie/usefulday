from PIL import Image
import sys
import argparse
import os

def has_transparency(img_path):
    with Image.open(img_path) as img:
        if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            alpha = img.split()[-1]
            if any(pixel < 255 for pixel in alpha.getdata()):
                return True
        return False
    
def webp_to_jpg(input_file, output_file=None):
    if output_file is None or not (output_file.lower().endswith('.jpg') or output_file.lower().endswith('.jpeg')):
        base, _ = os.path.splitext(input_file)
        output_file = f"{base}.jpg"
    if has_transparency(input_file):
        try:
            if input("Background color: black or white: ").lower() == "white":
                background_color=(255,255,255)
            else:
                background_color=(0,0,0)

            im = Image.open(input_file).convert("RGBA")

            background = Image.new("RGB", im.size, background_color)
            background.paste(im, (0,0), im)
            background.save(output_file, "jpeg", quality=95)
            print(f"Conversion succesful: {output_file}")
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
    else:
        try:
            im = Image.open(input_file).convert("RGB")
            im.save(output_file, "jpeg", quality=95)
            print(f"Conversion succesful: {output_file}")
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Convert .webp to .jpg")
    parser.add_argument('input_file', metavar='input_file', type=str, default=None, help='Input .webp file path')
    parser.add_argument('-o', '--output_file', type=str, default=None, help='Output .jpg file name')
    
    args = parser.parse_args()

    if os.path.isfile(args.input_file) and args.input_file.lower().endswith('.webp'):
        webp_to_jpg(args.input_file, args.output_file)
    else:
        print(f"Error: {args.input_file} does not exist or the extension is not .webp.")
        sys.exit(1)

if __name__ == '__main__':
    main()