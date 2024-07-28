import pandas as pd
import sys
import argparse
import os

def csv_to_excel(input_file, output_file):
    if output_file is None or not output_file.lower().endswith('.xlsx'):
        base, _ = os.path.splitext(input_file)
        output_file = f"{base}.xlsx"
    try:
        df = pd.read_csv(input_file, sep=None, engine='python')
        df.to_excel(output_file)
        print(f"Conversion succesful: {output_file}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Convert CSV into XLSX (Excel) file.")
    parser.add_argument('input_file', metavar='input_files', type=str, default=None, help='Input .csv file paths')
    parser.add_argument('-o', '--output_file', type=str, default=None, help='Output .xlsx file name')
    
    args = parser.parse_args()

    if os.path.isfile(args.input_file) and args.input_file.lower().endswith('.csv'):
        csv_to_excel(args.input_file, args.output_file)
    else:
        print(f"Error: {args.input_file} does not exist.")
        sys.exit(1)

if __name__ == '__main__':
    main()