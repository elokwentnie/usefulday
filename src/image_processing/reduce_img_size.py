from PIL import Image, ImageOps
import os
import argparse
import sys
import glob

def reduce_img_size(input_files, reduce_ratio=0.5, quality=85):
    for file in input_files:
        try:
            image = Image.open(file)
            original_width, original_height = image.size
            new_width = int(original_width * reduce_ratio)
            new_height = int(original_height * reduce_ratio)

            size = (new_width, new_height)
            output_file = os.path.splitext(file)[0] + "-reduced.jpg"

            resized_image = ImageOps.contain(image, size)
            resized_image.save(output_file, "JPEG", quality=quality)

            print(f"Reduced size of {file} for {round(reduce_ratio * 100),2}% and saved to {output_file}")
        except Exception as e:
            print(f"Failed to reduce size of {file}: {e}")

def range_limited_float_type(arg):
    """ Type function for argparse - a float within some predefined bounds """
    try:
        f = float(arg)
    except ValueError:
        raise argparse.ArgumentTypeError("Must be a floating point number")

    if f < 0 or f > 100:
        raise argparse.ArgumentTypeError("Argument must be between 0 and 100")

    return f

def main():
    parser = argparse.ArgumentParser(description="Convert .HEIC files to .jpg.")
    parser.add_argument('-f', '--input_files', metavar='input_files', type=str, nargs='+', default=None, help='Input .jpg file paths')
    parser.add_argument('-d', '--input_directory', type=str, default=None, help='Input directory with .jpg files inside')
    parser.add_argument('-s', '--reduce_ratio', type=range_limited_float_type, default=50, help='How much percentage do you want to reduce your image.')
    parser.add_argument('-q', '--quality', type=int, default=85, help='JPEG quality level from 1 to 100')

    args = parser.parse_args()
    
    reduce_ratio = 1- round(args.reduce_ratio / 100, 2)

    if args.input_files != None:
        for path in args.input_files:
            if not os.path.isfile(path):
                print(f"Error: {path} does not exist.")
                sys.exit(1)
            if not (os.path.splitext(path)[1].lower() == ".jpg" or os.path.splitext(path)[1].lower() == ".jpeg"):
                print(f"Error: {path} - is not jpg/jpeg.")
                sys.exit(1)
        reduce_img_size(args.input_files, reduce_ratio, args.quality)
    elif args.input_directory != None:
        input_files = []
        for file_path in glob.glob(os.path.join(args.input_directory, '*')):
            if os.path.isfile(file_path) and (file_path.lower().endswith('.jpg') or file_path.lower().endswith('.jpeg')):
                input_files.append(file_path)
        if not input_files:
            print(f"No .jpg / .jpeg files found in directory {args.input_directory}")
            sys.exit(1)
        reduce_img_size(input_files, reduce_ratio, args.quality)
    else:
        print("Error: Either --input_files or --input_directory must be provided.")
        sys.exit(1)

if __name__ == '__main__':
    main()