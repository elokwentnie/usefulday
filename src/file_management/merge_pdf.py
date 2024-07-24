import PyPDF2
import sys
import argparse
import os
import glob

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
    parser.add_argument('-f', '--input_files', metavar='input_files', type=str, nargs='+', default=None, help='Input .pdf file paths')
    parser.add_argument('-d', '--input_directory', type=str, default=None, help='Input directory with .pdf files inside')
    parser.add_argument('-o', '--output_name', type=str, default="merged.pdf", help='Output PDF file path')
    
    args = parser.parse_args()

    if args.input_files != None:
        for path in args.input_files:
            if not os.path.isfile(path):
                print(f"Error: {path} does not exist.")
                sys.exit(1)
        base_path = os.path.dirname(args.input_files[0])
        output_file = os.path.join(base_path, args.output_name)
        merge_pdf(args.input_files, output_file)
    elif args.input_directory != None:
        input_files = []
        for file_path in glob.glob(os.path.join(args.input_directory, '*')):
            if os.path.isfile(file_path) and file_path.lower().endswith('.pdf'):
                input_files.append(file_path)
        if not input_files:
            print(f"No .pdf files found in directory {args.input_directory}")
            sys.exit(1)
        merge_pdf(input_files, os.path.join(args.input_directory, args.output_name))
    else:
        print("Error: Either --input_files or --input_directory must be provided.")
        sys.exit(1)


if __name__ == '__main__':
    main()