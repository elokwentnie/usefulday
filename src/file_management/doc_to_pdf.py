from docx2pdf import convert
import sys
import argparse
import os

def doc_to_pdf(input_file, output_file):
    if output_file==None or output_file.split(".")[-1]!="pdf":
        output_file=input_file.split(".")[0] + ".pdf"
    convert(input_file, output_file)
    print(f"{input_file} converted successfully into {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Convert DOCX / DOC into PDF")
    parser.add_argument('input_file', metavar='input_files', type=str, default=None, help='Input .docx / .doc file paths')
    parser.add_argument('-o', '--output_file', type=str, default=None, help='Output .pdf file name')
    
    args = parser.parse_args()

    if os.path.isfile(args.input_file) and (args.input_file.lower().endswith('.docx') or args.input_file.lower().endswith('.doc')):
        doc_to_pdf(args.input_file, args.output_file)
    else:
        print(f"Error: {args.input_file} does not exist.")
        sys.exit(1)

if __name__ == '__main__':
    main()