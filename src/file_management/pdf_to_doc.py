from pdf2docx import parse
import sys
import argparse
import os

def pdf_to_docx(input_file, output_file):
    if output_file==None or output_file.split(".")[-1]!="docx":
        output_file=input_file.split(".")[0] + ".docx"
    parse(input_file, output_file)
    print(f"{input_file} converted successfully into {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Covert PDF into DOCX.")
    parser.add_argument('input_file', metavar='input_files', type=str, default=None, help='Input .PDF file paths')
    parser.add_argument('-o', '--output_file', type=str, default=None, help='Output .DOCX file name')
    
    args = parser.parse_args()

    if os.path.isfile(args.input_file) and args.input_file.lower().endswith('.pdf'):
        pdf_to_docx(args.input_file, args.output_file)
    else:
        print(f"Error: {args.input_file} does not exist.")
        sys.exit(1)

if __name__ == '__main__':
    main()