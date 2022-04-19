from src.writer import writer
import argparse

processor = writer()
parser = argparse.ArgumentParser(description='David to Mindustry David Instructions', usage='%(prog)s [options]')
parser.add_argument('file', type=str, help='File to be parsed')

args = parser.parse_args()

with open(args.file, 'r') as file:
	processor.fullwrite(file.readlines())

print(processor.output)