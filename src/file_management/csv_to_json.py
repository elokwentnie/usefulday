import pandas as pd
import sys
import argparse
import os

def csv_to_json(input_file, output_file):
    if output_file is None or not output_file.lower().endswith('.json'):
        base, _ = os.path.splitext(input_file)
        output_file = f"{base}.json"
    try:
        df = pd.read_csv(input_file, sep=None, engine='python')
        df.rename(columns={col:col.strip() for col in df.columns}, inplace=True)
        df.to_json(output_file, indent=4, orient='records', lines=True)
        print(f"Conversion succesful: {output_file}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Convert CSV into JSON file.")
    parser.add_argument('input_file', metavar='input_files', type=str, default=None, help='Input .csv file paths')
    parser.add_argument('-o', '--output_file', type=str, default=None, help='Output .json file name')
    
    args = parser.parse_args()

    if os.path.isfile(args.input_file) and args.input_file.lower().endswith('.csv'):
        csv_to_json(args.input_file, args.output_file)
    else:
        print(f"Error: {args.input_file} does not exist.")
        sys.exit(1)

if __name__ == '__main__':
    main()