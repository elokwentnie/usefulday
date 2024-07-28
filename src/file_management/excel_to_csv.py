import pandas as pd
import sys
import argparse
import os

def excel_to_csv(input_file, separator, output_file):
    if output_file is None or not output_file.lower().endswith('.csv'):
        base, _ = os.path.splitext(input_file)
        output_file = f"{base}.csv"
    try:
        df = pd.read_excel(input_file)
        df_cleaned = df.dropna(axis=1, how='all')
        df_cleaned.to_csv(output_file, index=False, sep=separator)
        print(f"Conversion succesful: {output_file}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def parse_separator_argument(arg):
    """ Parse and validate separator argument """
    csv_separators = [
    ',',     # Comma
    ';',     # Semicolon
    '\t',    # Tab
    '|',     # Pipe
    ' ',     # Space
    '^',     # Caret
    '~',     # Tilde
    ':',     # Colon
    '#',     # Hash/Pound
    '@',     # At sign
    '!',     # Exclamation mark
    ]
    try:
        sep = str(arg)
    except ValueError:
        raise argparse.ArgumentTypeError("Must be a string/character argument.")

    if sep not in csv_separators:
        raise argparse.ArgumentTypeError(f"Invalid separator '{sep}'. Must be one of {', '.join(repr(s) for s in csv_separators)}.")

    return sep

def main():
    parser = argparse.ArgumentParser(description="Convert XLSX (Excel) into CSV file.")
    parser.add_argument('input_file', metavar='input_files', type=str, default=None, help='Input .xlsx file paths')
    parser.add_argument('-o', '--output_file', type=str, default=None, help='Output .csv file name')
    parser.add_argument('-s', '--separator', type=parse_separator_argument, default=',', help="Separator for final .csv file (default: ',').")
    
    args = parser.parse_args()

    if os.path.isfile(args.input_file) and args.input_file.lower().endswith('.xlsx'):
        excel_to_csv(args.input_file, args.separator, args.output_file)
    else:
        print(f"Error: {args.input_file} does not exist.")
        sys.exit(1)

if __name__ == '__main__':
    main()