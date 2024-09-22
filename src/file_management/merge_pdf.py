import sys
import argparse
from pathlib import Path
from PyPDF2 import PdfMerger
from PyPDF2.errors import PdfReadError

def merge_pdf(input_files: list[Path], output_path: Path) -> None:
    merger = PdfMerger()
    for pdf_file in input_files:
        try:
            merger.append(str(pdf_file))
        except PdfReadError:
            print(f"Error: '{pdf_file}' is not a valid PDF file or is corrupted. Skipping.")
        except Exception as e:
            print(f"Unexpected error while reading '{pdf_file}': {e}")
    try:
        merger.write(str(output_path))
        print(f"PDFs merged successfully into '{output_path}'")
    except Exception as e:
        print(f"Error writing output PDF: {e}")
        sys.exit(1)
    finally:
        merger.close()

def main():
    parser = argparse.ArgumentParser(description="Merge multiple PDF files into a single PDF.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f', '--input_files', type=Path, nargs='+', help='Input PDF file paths')
    group.add_argument('-d', '--input_directory', type=Path, help='Directory containing PDF files to merge')
    parser.add_argument('-o', '--output', type=Path, default=Path('merged.pdf'), help='Output PDF file path')

    args = parser.parse_args()

    if args.input_files:
        input_files = args.input_files
    elif args.input_directory:
        if not args.input_directory.is_dir():
            print(f"Error: '{args.input_directory}' is not a valid directory.")
            sys.exit(1)
        input_files = sorted(args.input_directory.glob('*.pdf'))
        if not input_files:
            print(f"No PDF files found in directory '{args.input_directory}'")
            sys.exit(1)
    else:
        print("Error: Either input files or input directory must be provided.")
        sys.exit(1)

    # Validate that input files exist and are files
    for pdf_file in input_files:
        if not pdf_file.is_file():
            print(f"Error: '{pdf_file}' does not exist or is not a file.")
            sys.exit(1)

    merge_pdf(input_files, args.output)

if __name__ == '__main__':
    main()