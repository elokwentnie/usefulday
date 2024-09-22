import sys
import argparse
from pathlib import Path
from PIL import Image, UnidentifiedImageError
import img2pdf

def img_to_pdf(input_file: Path, output_file: Path = None) -> None:
    if output_file is None:
        output_file = input_file.with_suffix('.pdf')
    try:
        # Ensure the image can be opened
        with Image.open(input_file) as img:
            pass  # Image successfully opened

        # Convert the image to PDF
        with open(output_file, "wb") as f:
            f.write(img2pdf.convert(str(input_file)))
        print(f"Conversion successful: {output_file}")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except UnidentifiedImageError:
        print(f"Error: Cannot identify image file '{input_file}'.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Convert an image file to PDF.")
    parser.add_argument('input_file', type=Path, help='Path to the input image file')
    parser.add_argument('-o', '--output_file', type=Path, default=None, help='Path for the output PDF file')
    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output_file

    # Validate the input file
    if not input_file.is_file():
        print(f"Error: '{input_file}' does not exist or is not a file.")
        sys.exit(1)

    img_to_pdf(input_file, output_file)

if __name__ == '__main__':
    main()