from pathlib import Path
from typing import Union, Literal, List
import sys
import argparse
import os

from PyPDF2 import PdfWriter, PdfReader

def add_watermark(
    input_file: Path,
    watermark_pdf: Path,
    page_indices: Union[Literal["ALL"], List[int]] = "ALL",
):
    reader = PdfReader(input_file)
    if page_indices == "ALL":
        page_indices = list(range(0, len(reader.pages)))

    output_file = input_file.with_stem(f"{input_file.stem}-watermark")

    writer = PdfWriter()
    for index in page_indices:
        content_page = reader.pages[index]
        mediabox = content_page.mediabox

        # You need to load it again, as the last time it was overwritten
        reader_stamp = PdfReader(watermark_pdf)
        watermark_page = reader_stamp.pages[0]

        content_page.merge_page(watermark_page)  # Merge watermark into content page
        content_page.mediabox = mediabox  # Ensure the content page keeps its mediabox
        writer.add_page(content_page)

    with open(output_file, "wb") as fp:
        writer.write(fp)

def main():
    parser = argparse.ArgumentParser(description="Add watermark to PDF. The watermark should be pdf file with the same dimensions as the input PDF.")
    parser.add_argument('input_file', metavar='input_file', type=str, help='Input .PDF file path')
    parser.add_argument('-w', '--watermark', type=str, required=True, help='Watermark file')
    
    args = parser.parse_args()

    if not os.path.isfile(args.input_file) or not args.input_file.lower().endswith('.pdf'):
        print(f"Error: {args.input_file} does not exist or it is not a PDF file.")
        sys.exit(1)

    if not os.path.isfile(args.watermark) or not args.watermark.lower().endswith('.pdf'):
        print(f"Error: {args.watermark} does not exist or it is not a PDF file.")
        sys.exit(1)

    add_watermark(Path(args.input_file), Path(args.watermark))

if __name__ == '__main__':
    main()