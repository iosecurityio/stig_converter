""" Description: This script is used to test the stig_converter.py script"""

import argparse
import sys

def main():
    """Main function to run the script"""

    parser = argparse.ArgumentParser(
        description="Process input file and generate output.",
        usage="%(prog)s -i <input file> -o <output directory>",
    )
    parser.add_argument("-i", "--input", type=str, help="The input file to convert")
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="The output directory to save the converted file to",
    )
    args = parser.parse_args()
    # check that there are no more than 2 arguments
    if len(sys.argv) > 5:
        print("Too many arguments")
        exit()
    
    if args.input is None:
        print("Please provide an input file")
        exit()
    if args.output is None:
        print("Please provide an output directory")
        exit()
    input_file = args.input
    output_dir = args.output

    print(input_file + "Input file")
    print(output_dir + "Output directory")


if __name__ == "__main__":
    main()
