from PyPDF2 import PdfReader, PdfWriter
import sys
import argparse
import os

def split_pdf(input_file, parts):
    base, _ = os.path.splitext(input_file)

    try:
        reader = PdfReader(input_file)
        if not parts:
            for i, page in enumerate(reader.pages):
                output_file = f"{base}-part_{i+1}.pdf"
                write_pages_to_pdf([page], output_file)
        else:
            for i, part in enumerate(parts):
                output_file = f"{base}-part_{i+1}.pdf"
                pages_to_write = [reader.pages[page_num] for page_num in part]
                write_pages_to_pdf(pages_to_write, output_file)
        
        print("Successfully split the PDF into parts.")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def write_pages_to_pdf(pages, output_file):
    writer = PdfWriter()
    for page in pages:
        writer.add_page(page)
    with open(output_file, "wb") as file:
        writer.write(file)
    print(f"Succesfuly created: {output_file}.")

def parse_parts_argument(arg):
    """ Parse and validate parts argument """
    try:
        num_parts = int(arg)
        if num_parts < 1:
            raise argparse.ArgumentTypeError("Argument must be bigger than 1")
        return num_parts
    except ValueError:
        raise argparse.ArgumentTypeError("Must be an integer")

def get_splitting_parts(pdf_length, num_parts):
    """ Calculate page ranges for splitting the PDF """
    n, remainder = divmod(pdf_length, num_parts)
        
    return [
        list(range(start, start + n + (1 if i < remainder else 0)))
        for i, start in enumerate(range(0, pdf_length, n+1))
    ]


def main():
    parser = argparse.ArgumentParser(description="Split pdf page by page into seperate file (default), or split it in given number of parts.")
    parser.add_argument('input_file', metavar='input_file', type=str, default=None, help='Input .PDF file path')
    parser.add_argument('-p', '--parts', type=parse_parts_argument, default=None, help='Number of parts that you want to split pdf.')
    
    args = parser.parse_args()

    if not os.path.isfile(args.input_file) or not args.input_file.lower().endswith('.pdf'):
        print(f"Error: {args.input_file} does not exist or it is not PDF file.")
        sys.exit(1)
    
    if args.parts:
        reader = PdfReader(args.input_file)
        pdf_length = len(reader.pages)

        if args.parts > pdf_length:
            print("Number of parts cannot exceed the number of pages. Splitting into individual pages.")
            parts = None
        else:
            parts = get_splitting_parts(pdf_length, args.parts)
    else:
        parts = None

    split_pdf(args.input_file, parts)

if __name__ == '__main__':
    main()