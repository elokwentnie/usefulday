from PIL import Image
import pillow_heif
import sys
import os
import glob
import argparse

def heic_to_jpg(input_files, output_directory):
    for file in input_files:
        try:
            heif_file = pillow_heif.read_heif(file)
            image = Image.frombytes(
                heif_file.mode,
                heif_file.size,
                heif_file.data,
                "raw",
                heif_file.mode,
                heif_file.stride,
            )
            file_name = file.split(".")[0] + ".jpg"
            output_file = os.path.join(output_directory, file_name)
            image.save(output_file, "jpeg")
            print(f"Converted {file} to {output_file}")
        except Exception as e:
            print(f"Failed to convert {file}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Convert .HEIC files to .jpg.")
    parser.add_argument('-f', '--input_files', metavar='input_files', type=str, nargs='+', default=None, help='Input .HEIC file paths')
    parser.add_argument('-d', '--input_directory', type=str, default=None, help='Input directory with .HEIC files inside')
    parser.add_argument('-o', '--output', type=str, default="", help='Output directory')

    args = parser.parse_args()

    if args.input_files != None:
        for path in args.input_files:
            if not os.path.isfile(path):
                print(f"Error: {path} does not exist.")
                sys.exit(1)
        heic_to_jpg(args.input_files, args.output)
    elif args.input_directory != None:
        input_files = []
        for file_path in glob.glob(os.path.join(args.input_directory, '*')):
            if os.path.isfile(file_path) and file_path.lower().endswith('.heic'):
                input_files.append(file_path)
        if not input_files:
            print(f"No .HEIC files found in directory {args.input_directory}")
            sys.exit(1)
        heic_to_jpg(input_files, args.output)
    else:
        print("Error: Either --input_files or --input_directory must be provided.")
        sys.exit(1)

if __name__ == '__main__':
    main()