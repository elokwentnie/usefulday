from PIL import Image
import sys
import argparse
import os

def jpg_to_png(input_file, output_file=None, quality=85):
    if output_file is None or not output_file.lower().endswith('.png'):
        base, _ = os.path.splitext(input_file)
        output_file = f"{base}.png"
    try:    
        im = Image.open(input_file).convert("RGB")
        im.save(output_file, "png", quality=quality)
        print(f"Conversion succesful: {output_file}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def range_limited_int_type(arg):
    """ Type function for argparse - an int within some predefined bounds """
    try:
        i = int(arg)
    except ValueError:
        raise argparse.ArgumentTypeError("Must be a number")

    if i < 0 or i > 100:
        raise argparse.ArgumentTypeError("Argument must be between 0 and 100")

    return i

def main():
    parser = argparse.ArgumentParser(description="Convert .jpg to .png")
    parser.add_argument('input_file', metavar='input_file', type=str, default=None, help='Input .jpg file path')
    parser.add_argument('-o', '--output_file', type=str, default=None, help='Output .png file name')
    parser.add_argument('-q', '--quality', type=range_limited_int_type, default=85, help='Quality: 0-100')
    
    args = parser.parse_args()

    if os.path.isfile(args.input_file) and (args.input_file.lower().endswith('.jpg') or args.input_file.lower().endswith('.jpeg')):
        jpg_to_png(args.input_file, args.output_file)
    else:
        print(f"Error: {args.input_file} does not exist or the extension is not .jpg/.jpeg.")
        sys.exit(1)

if __name__ == '__main__':
    main()