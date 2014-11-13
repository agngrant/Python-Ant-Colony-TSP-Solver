import pickle
import argparse
import csv

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("in_file", help="Name of csv data file")
    parser.add_argument("out_file", help="Name of output pickle data file")
    args = parser.parse_args()
    process(args.in_file, args.out_file)

def process(infilename, outfilename):
    csvfile = open(infilename, 'rU')
    csvreader = csv.reader(csvfile)
    distance_mat = []
    distance_mat.append(next(csvreader))
    distances =[]
    for row in csvreader:
        print type(row)
	distances.append([int(i) for i in row])
    distance_mat.append(distances)
    csvfile.close()
    pickle.dump(distance_mat, open(outfilename, 'wb'))    

main()

