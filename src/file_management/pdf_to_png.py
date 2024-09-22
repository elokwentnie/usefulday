import sys
import argparse
from pathlib import Path
from pdf2image import convert_from_path
from zipfile import ZipFile

def pdf_to_png(input_file: Path, zip_output: bool = False) -> None:
    base_name = input_file.stem
    output_dir = input_file.parent

    try:
        # Convert PDF to a list of images
        pages = convert_from_path(str(input_file))

        image_files = []
        for i, page in enumerate(pages, start=1):
            output_file = output_dir / f"{base_name}_page_{i}.png"
            page.save(output_file, "PNG")
            image_files.append(output_file)
            print(f"Successfully created: {output_file}")

        if zip_output:
            zip_filename = output_dir / f"{base_name}_images.zip"
            with ZipFile(zip_filename, 'w') as zipf:
                for image_file in image_files:
                    zipf.write(image_file, arcname=image_file.name)
            print(f"Successfully zipped images into: {zip_filename}")
        else:
            print("Successfully converted PDF pages to PNG images.")
    except Exception as e:
        print(f"Error processing {input_file}: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description="Convert PDF pages to individual PNG images, with an option to zip the output."
    )
    parser.add_argument('input_file', type=Path, help='Path to the input PDF file')
    parser.add_argument(
        '-z', '--zip', action='store_true', help='Zip the output PNG files into a single archive.'
    )

    args = parser.parse_args()

    input_file = args.input_file
    zip_output = args.zip

    # Validate the input file
    if not input_file.is_file() or input_file.suffix.lower() != '.pdf':
        print(f"Error: '{input_file}' does not exist or is not a PDF file.")
        sys.exit(1)

    pdf_to_png(input_file, zip_output)

if __name__ == '__main__':
    main()