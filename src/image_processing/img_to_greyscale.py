from PIL import Image, ImageOps
import sys
import os
import argparse

def img_to_greyscale(input_file, output_file=None, quality=85):
    if output_file is None:
        base, ext = os.path.splitext(input_file)
        output_file = f"{base}-greyscale{ext}"
    try:
        with Image.open(input_file) as image:
            image_gray = ImageOps.grayscale(image)
            image_gray.save(output_file, quality=quality)
            print(f"Conversion succesful: {output_file}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def is_image(file_path):
    try:
        with Image.open(file_path) as img:
            return True
    except (IOError, Image.UnidentifiedImageError) as e:
        print(f"Error: {e}")
        return False
    
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
    parser = argparse.ArgumentParser(description="Convert image file to grey scale")
    parser.add_argument('input_file', metavar='input_file', type=str, default=None, help='Input: image file path')
    parser.add_argument('-o', '--output_file', type=str, default=None, help='Output file name')
    parser.add_argument('-q', '--quality', type=range_limited_int_type, default=85, help='Quality: 0-100')
    
    args = parser.parse_args()

    if os.path.isfile(args.input_file) and is_image(args.input_file):
        img_to_greyscale(args.input_file, args.output_file, args.quality)
    else:
        print(f"Error: {args.input_file} does not exist or is not an image.")
        sys.exit(1)

if __name__ == '__main__':
    main()