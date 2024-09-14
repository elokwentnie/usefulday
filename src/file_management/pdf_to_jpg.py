from pdf2image import convert_from_path
from zipfile import ZipFile 
import sys
import argparse
import os

def pdf_to_jpg(input_file, zip=False):
    base, _ = os.path.splitext(input_file)
    try:
        pages = convert_from_path(input_file)
        if not zip:
            write_pages_to_jpg(pages, base)
            print("Successfully split the PDF into png files.")
        else:
            output_zip = f"{base}-png-packed.tar"
            with ZipFile(output_zip, 'w') as zip_object:
                write_pages_to_jpg(pages, base, zip_object)
            print(f"Successfully split the PDF into png files and zipped into {output_zip}.")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def write_pages_to_jpg(pages, base, zip_object=False):
     for i, page in enumerate(pages):
        output_file = f"{base}-part_{i+1}.jpg"
        page.save(output_file, "JPEG")
        print(f"Succesfuly created: {output_file}.")
        if zip_object:
            zip_object.write(output_file, arcname=f"{base}-part_{i+1}.png")

def main():
    parser = argparse.ArgumentParser(description="Split pdf page by page into seperate png files (default), you can zip the output.")
    parser.add_argument('input_file', metavar='input_file', type=str, default=None, help='Input .PDF file path')
    parser.add_argument('-z', '--zip', action='store_true', help='Use if you want to zip the output.')
    
    args = parser.parse_args()

    if not os.path.isfile(args.input_file) or not args.input_file.lower().endswith('.pdf'):
        print(f"Error: {args.input_file} does not exist or it is not PDF file.")
        sys.exit(1)

    pdf_to_jpg(args.input_file, args.zip)

if __name__ == '__main__':
    main()