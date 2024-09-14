import pandas as pd
import json
import sys
import argparse
import os

def json_to_csv(input_file, output_file):
    if output_file is None or not output_file.lower().endswith('.csv'):
        base, _ = os.path.splitext(input_file)
        output_file = f"{base}.csv"
    try:
        with open(input_file) as data_file:    
            data = json.load(data_file) 
        df_json = pd.json_normalize(data)
        df_json.to_csv(output_file)
        print(f"Conversion succesful: {output_file}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Convert XLSX (Excel) into CSV file.")
    parser.add_argument('input_file', metavar='input_files', type=str, default=None, help='Input .json file paths')
    parser.add_argument('-o', '--output_file', type=str, default=None, help='Output .csv file name')
    
    args = parser.parse_args()

    if os.path.isfile(args.input_file) and args.input_file.lower().endswith('.json'):
        json_to_csv(args.input_file, args.output_file)
    else:
        print(f"Error: {args.input_file} does not exist.")
        sys.exit(1)

if __name__ == '__main__':
    main()