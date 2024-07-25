from PIL import Image
import sys


def has_transparency(img_path):
    with Image.open(img_path) as img:
        if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            alpha = img.split()[-1]
            if any(pixel < 255 for pixel in alpha.getdata()):
                return True
        return False
    
def webp_to_jpg(input_path, output_path=None):
    if output_path==None:
            output_path=input_path.split(".")[0] + ".jpg"
    if has_transparency(input_path):
        if input("Background color: black or white: ").lower() == "white":
            background_color=(255,255,255)
        else:
            background_color=(0,0,0)
        im = Image.open(input_path).convert("RGBA")
        background = Image.new("RGB", im.size, background_color)
        background.paste(im, (0,0), im)

        background.save(output_path, "jpeg")
    else:
        im = Image.open(input_path).convert("RGB")
        im.save(output_path, "jpeg", quality=95)

def main():
    if len(sys.argv) < 2:
        print("Usage: webp_to_jpg <input_path> [output_path]")
        print(f"Arguments received: {sys.argv}")
        sys.exit(1)
    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    webp_to_jpg(input_path, output_path)

if __name__ == '__main__':
    main()