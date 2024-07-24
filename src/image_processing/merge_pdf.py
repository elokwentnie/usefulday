import PyPDF2
import sys
import argparse
import os

def merge_pdf(input_files, output_path):
    pdf_merge = PyPDF2.PdfMerger()
    for pdf in input_files:
        try:
            with open(pdf, 'rb') as pdf_file:
                pdf_merge.append(PyPDF2.PdfReader(pdf_file))
        except PyPDF2.errors.PdfReadError:
            print(f"Error: {pdf} is not a valid PDF file or is corrupted. Skipping.")
        except Exception as e:
            print(f"Unexpected error while reading {pdf}: {e}")
    pdf_merge.write(output_path)
    print(f"PDFs merged successfully into {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Merge multiple PDF files into a single PDF.")
    parser.add_argument('input_files', metavar='input_files', type=str, nargs='+', help='Input PDF file paths')
    parser.add_argument('-o', '--output', type=str, default='merged.pdf', help='Output PDF file path')
    
    args = parser.parse_args()

    # Ensure all input files exist
    for path in args.input_files:
        if not os.path.isfile(path):
            print(f"Error: {path} does not exist.")
            sys.exit(1)
    
    merge_pdf(args.input_files, args.output)

if __name__ == '__main__':
    main()