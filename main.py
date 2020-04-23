import csv
import json
import parser
import argparse

sumNumbersParser = None
genSubParser = None
jsonTocsvParser = None

def sumNumbers(args):
    print(f'Sum: {sum(args.numbers)}')


def generateSeries(args):
    ansList = []
    try:
        start = args.start
        step = args.step
        stop = args.stop
        while start <= stop:
            ansList.append(start)
            start += step
        print("Generated Sequence:", ansList)
    except Exception as e:
        print(e)
        print("Expected Arguments --start <int>,--stop <int>,--step <int (Optional)>")

def converter(args):
    fileInput = args.input
    fileOutput = args.output
    try:

        # Open File
        with open(fileInput) as json_file:
            data = json.load(json_file)

        # Open OutputFile with write Attribute
        data_file = open(fileOutput, 'w')
        csv_writer = csv.writer(data_file)
        csv_writer.writerow(data.keys())
        csv_writer.writerow(iter(data.values()))
        data_file.close()
    except Exception as e:
        print("File Error....Check input file\n", e)
        parser.print()


def main():
    parser = argparse.ArgumentParser(description="Parser Program")

    subparser = parser.add_subparsers(help="Sub parser for program")

    sumNumbersParser = subparser.add_parser('sum', help='Sum Numbers')
    genSubParser = subparser.add_parser('generate', help='generate String')
    jsonTocsvParser = subparser.add_parser('convert', help='convert json to csv')

    sumNumbersParser.add_argument('numbers', type=int, nargs='+')
    sumNumbersParser.set_defaults(func=sumNumbers)

    genSubParser.add_argument('--start', type=int)
    genSubParser.add_argument('--stop', type=int)
    genSubParser.add_argument('--step', type=int, default=1, required=bool(0))
    genSubParser.set_defaults(func=generateSeries)

    jsonTocsvParser.add_argument('-i', '--input', type=str)
    jsonTocsvParser.add_argument('-o', '--output', type=str)
    jsonTocsvParser.set_defaults(func=converter)

    try:
        args2 = parser.parse_args()
        args2.func(args2)
    except Exception as e:
        print(e)
        parser.print_help()


if __name__ == "__main__":
    main()
