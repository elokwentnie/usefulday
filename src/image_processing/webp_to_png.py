from PIL import Image
import sys
import argparse
import os

def webp_to_png(input_file, output_file):
    if output_file is None or not output_file.lower().endswith('.png'):
        base, _ = os.path.splitext(input_file)
        output_file = f"{base}.png"
    try:    
        im = Image.open(input_file).convert("RGBA")
        im.save(output_file, "png")
        print(f"Conversion succesful: {output_file}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Convert .webp to .png")
    parser.add_argument('input_file', metavar='input_file', type=str, default=None, help='Input .webp file path')
    parser.add_argument('-o', '--output_file', type=str, default=None, help='Output .png file name')
    
    args = parser.parse_args()

    if os.path.isfile(args.input_file) and args.input_file.lower().endswith('.webp'):
        webp_to_png(args.input_file, args.output_file)
    else:
        print(f"Error: {args.input_file} does not exist or the extension is not .webp.")
        sys.exit(1)

if __name__ == '__main__':
    main()