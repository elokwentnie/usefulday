from PyPDF2 import PdfReader, PdfWriter
from PIL import Image
import sys
import argparse
import os

def png_to_pdf(png_file, pdf_file):
    image = Image.open(png_file)
    pdf_path = pdf_file
    image.convert('RGB').save(pdf_path, "PDF", resolution=100.0)

def add_watermark(input_file, watermark):
    base, _ = os.path.splitext(input_file)
    output_file = f"{base}-watermark.pdf"

    try:
        with open(input_file, "rb") as input_file, open(watermark, "rb") as watermark_file:
            input_file = PdfReader(input_file)
            watermark_pdf = PdfReader(watermark_file)
            watermark_page = watermark_pdf.pages[0]

            output = PdfWriter()

            for page in input_file.pages:
                page.merge_page(watermark_page)
                output.add_page(page)

            with open(output_file, "wb") as merged_file:
                output.write(merged_file)
        
        print(f"Successfully added watermark to PDF, saved new file into: {output_file}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Add watermark to all pdf pages.")
    parser.add_argument('input_file', metavar='input_file', type=str, default=None, help='Input .PDF file path')
    parser.add_argument('watermark_file', metavar='watermark_file', type=str, default=None, help='Input watermark .PDF file path')
    
    args = parser.parse_args()

    if not os.path.isfile(args.input_file) or not args.input_file.lower().endswith('.pdf'):
        print(f"Error: {args.input_file} does not exist or it is not PDF file.")
        sys.exit(1)

    if not os.path.isfile(args.watermark_file):
        print(f"Error: {args.watermark_file} does not exist.")
        sys.exit(1)

    if args.watermark_file.lower().endswith('.png'):
        watermark_pdf = "watermark_temp.pdf"
        png_to_pdf(args.watermark_file, watermark_pdf)
        add_watermark(args.input_file, watermark_pdf)
        os.remove(watermark_pdf)

    add_watermark(args.input_file, args.watermark_file)

if __name__ == '__main__':
    main()