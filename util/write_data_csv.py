import csv
import pickle
import argparse
import sys


def main(args):
    """Get one line
       from stdin
       and return it."""
    parser = argparse.ArgumentParser()
    parser.add_argument("in_file", help="Name of pickled data file")
    parser.add_argument("out_file", help="Name of output csv data file")
    args = parser.parse_args()
    process(args.in_file, args.out_file)


def process(infilename, outfilename):
    stuff = pickle.load(open(infilename, "r"))
    csvfile = open(outfilename, 'w')
    filewriter = csv.writer(csvfile)
    filewriter.writerow(stuff[0])
    for drow in stuff[1]:
        filewriter.writerow(drow)
    csvfile.close()


if __name__ == "__main__":
    main(sys.argv[1:])
