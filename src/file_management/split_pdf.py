from PyPDF2 import PdfReader, PdfWriter
import sys
import argparse
import os

def split_pdf(input_file, parts):
    base, _ = os.path.splitext(input_file)
    try:
        reader = PdfReader(input_file)
        if parts:
            for i, part in enumerate(parts):
                output_file = base + f"-part_{i+1}" + ".pdf"
                writer = PdfWriter()
                for page in reader.pages[part[0]:part[0]+len(part)]:
                    writer.add_page(page)
                with open(output_file, "wb") as f:
                    writer.write(f)
                print(f"Succesfuly splitted: {output_file}")
        else:
            for i, page in enumerate(reader.pages):
                writer = PdfWriter()
                output_file = base + f"-part_{i+1}" + ".pdf"
                writer.add_page(page)
                with open(output_file, "wb") as f:
                    writer.write(f)
                print(f"Succesfuly splitted: {output_file}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def range_limited_int_type(arg):
    """ Type function for argparse - an int within some predefined bounds """
    try:
        i = int(arg)
    except ValueError:
        raise argparse.ArgumentTypeError("Must be a number")

    if i < 1:
        raise argparse.ArgumentTypeError("Argument must be bigger than 1")
    
    return i

def main():
    parser = argparse.ArgumentParser(description="Split pdf page by page into seperate file (default), or split it in given number of parts.")
    parser.add_argument('input_file', metavar='input_file', type=str, default=None, help='Input .PDF file path')
    parser.add_argument('-p', '--parts', type=range_limited_int_type, default=None, help='Number of parts that you want to split pdf.')
    
    args = parser.parse_args()

    parts = args.parts

    if parts is not None:
        reader = PdfReader(args.input_file)
        pdf_length = len(reader.pages)
        if parts > pdf_length:
            parts = None
            print("Number of parts cannot be higher than maximum number of pages.")
            print("Splitting into single pages.")
        else:
            n, remainder = divmod(pdf_length, parts)
            
            parts = [
                list(range(start, start + n + (1 if i < remainder else 0)))
                for i, start in enumerate(range(0, pdf_length, n+1))
            ]

    if os.path.isfile(args.input_file) and args.input_file.lower().endswith('.pdf'):
        split_pdf(args.input_file, parts)
    else:
        print(f"Error: {args.input_file} does not exist or it is not PDF file.")
        sys.exit(1)

if __name__ == '__main__':
    main()