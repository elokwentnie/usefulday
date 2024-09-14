from PIL import Image
import pytesseract
import sys
import argparse
import os
from pathlib import Path

def extract_text_from_img(input_file, save_flag=False):
    try:    
        image = Image.open(input_file).convert("RGB")
        extracted_text = pytesseract.image_to_string(image)
        print(extracted_text)
        if save_flag:
            base, _ = os.path.splitext(input_file)
            output_file = f"{base}.txt"
            with open(output_file, 'w') as file:
                file.write(extracted_text)
                print(f"Successfully saved extracted text into txt file: {output_file}.")
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
    parser = argparse.ArgumentParser(description="Extract metadata from an .jpg image")
    parser.add_argument('input_file', metavar='input_file', type=str, default=None, help='Input image file path')
    parser.add_argument('-s', '--save', action='store_true', help='Enable save to output directory')
    
    args = parser.parse_args()

    if os.path.isfile(args.input_file) and is_image(args.input_file):
        extract_text_from_img(args.input_file, args.save)
    else:
        print(f"Error: {args.input_file} does not exist or the file is not an image.")
        sys.exit(1)

if __name__ == '__main__':
    main()