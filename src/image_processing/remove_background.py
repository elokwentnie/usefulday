import rembg
import numpy as np
import os
import argparse
from PIL import Image
import sys
import glob
    
def remove_background(input_files):
    for file in input_files:
        try:
            image = Image.open(file)
            file_ext = os.path.splitext(file)[1]
            output_file = os.path.splitext(file)[0] + "-background-removed" + file_ext
            input_array = np.array(image)
            output_array = rembg.remove(input_array)
            output_image = Image.fromarray(output_array)

            if output_image.mode == 'RGBA':
                # Remove alpha channel for JPEG or keep it for PNG
                if file_ext in ['.jpg', '.jpeg']:
                    # Convert RGBA to RGB
                    output_image = output_image.convert('RGB')

            output_image.save(output_file, quality=95)
            print(f"Bacground removal succesful: {output_file}")
        except Exception as e:
            print(f"Failed to remove background of {file}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Remove background from photos.")
    parser.add_argument('-f', '--input_files', metavar='input_files', type=str, nargs='+', default=None, help='Input file path(s)')
    parser.add_argument('-d', '--input_directory', type=str, default=None, help='Input directory with photos inside')

    args = parser.parse_args()
    
    if args.input_files != None:
        for path in args.input_files:
            if not os.path.isfile(path):
                print(f"Error: {path} does not exist.")
                sys.exit(1)
        remove_background(args.input_files)
    elif args.input_directory != None:
        input_files = []
        for file_path in glob.glob(os.path.join(args.input_directory, '*')):
            if os.path.isfile(file_path) and (file_path.lower().endswith('.jpg') or file_path.lower().endswith('.png')):
                input_files.append(file_path)
        if not input_files:
            print(f"No .jpg / .png files found in directory {args.input_directory}")
            sys.exit(1)
        remove_background(input_files)
    else:
        print("Error: Either --input_files or --input_directory must be provided.")
        sys.exit(1)

if __name__ == '__main__':
    main()