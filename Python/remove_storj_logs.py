import pandas as pd
import argparse
import sys

def remove_storagenode_rows_pandas(input_file, output_file):
    """
    Removes all rows from the input CSV file where the 'Process' column
    has the value 'storagenode' and writes the result to the output CSV file.

    :param input_file: Path to the input CSV file.
    :param output_file: Path to the output CSV file.
    """
    try:
        # Read the CSV file
        df = pd.read_csv(input_file)

        if 'Process' not in df.columns:
            print(f"Error: 'Process' column not found in {input_file}.")
            sys.exit(1)

        # Filter out rows where 'Process' is 'storagenode' (case-insensitive)
        initial_count = len(df)
        df_filtered = df[df['Process'].str.strip().str.lower() != 'storagenode']
        removed_count = initial_count - len(df_filtered)

        # Write the filtered DataFrame to the output CSV
        df_filtered.to_csv(output_file, index=False)

        print(f"Processed {initial_count} rows.")
        print(f"Removed {removed_count} rows where 'Process' == 'storagenode'.")
        print(f"Filtered data written to {output_file}.")

    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        print("Error: No data found in the input file.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied when accessing the file.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Remove rows with 'Process' == 'storagenode' from a CSV file using pandas.")
    parser.add_argument('input_file', help='Path to the input CSV file.')
    parser.add_argument('output_file', help='Path to the output CSV file.')

    args = parser.parse_args()

    remove_storagenode_rows_pandas(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
