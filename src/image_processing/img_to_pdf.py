from PIL import Image
import img2pdf
import sys
import os
import argparse

def img_to_pdf(input_file, output_file=None):
    if output_file is None:
        base, _ = os.path.splitext(input_file)
        output_file = f"{base}.pdf"
    try:
        with Image.open(input_file) as image:
            pdf = img2pdf.convert(image.filename)
            with open(output_file, "wb") as file:
                file.write(pdf)
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

def main():
    parser = argparse.ArgumentParser(description="Convert image file to .pdf")
    parser.add_argument('input_file', metavar='input_file', type=str, default=None, help='Input: image file path')
    parser.add_argument('-o', '--output_file', type=str, default=None, help='Output .pdf file name')
    
    args = parser.parse_args()

    if os.path.isfile(args.input_file) and is_image(args.input_file):
        img_to_pdf(args.input_file, args.output_file)
    else:
        print(f"Error: {args.input_file} does not exist or is not an image.")
        sys.exit(1)

if __name__ == '__main__':
    main()