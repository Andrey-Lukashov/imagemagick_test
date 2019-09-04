import subprocess
import sys
import json
import argparse
from os import path


def convert(input, output, size, transpose=None):
    if transpose:
        transpose = "-transpose"
    else:
        transpose = ""

    if not path.exists(input):
        print(input + " - input file doesn't exist or wrong path is provided")
        return False

    subprocess.call("convert " + input + " " + transpose + " -resize " + size + " " + output, shell=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--json')
    parser.add_argument('--input')
    parser.add_argument('--size')
    parser.add_argument('--output')
    parser.add_argument('--transpose')
    args = parser.parse_args()

    if args.json:
        json_file = open(args.json)

        if not path.exists(args.json):
            sys.exit("Wrong JSON file path")

        json_array = json.load(json_file)

        for file in json_array:
            transpose = None
            if 'transpose' in file:
                transpose = True

            convert(file['input'], file['output'], file['size'], transpose)
        sys.exit("Successfully converted images in the json file")

    if len(sys.argv) > 2:
        if not args.input:
            sys.exit("You must provide path to input file")
        if not args.size:
            sys.exit("You must provide image size/scaling factor")
        if not args.output:
            sys.exit("You must provide output file name")

        transpose = None
        if args.transpose:
            transpose = True

        convert(args.input, args.output, args.size, transpose)

        sys.exit("Successfully converted image")

    sys.exit("You must pass correct arguments to the script.")

#TODO --help option explaining arguments
#TODO documentation and commenting
#TODO unit testing