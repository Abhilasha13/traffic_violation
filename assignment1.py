#!/usr/bin/python

import sys, getopt
import csv
from pyproj import Proj, transform

def get_input_output_file(argv):
    inf = ''
    outf = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('python assignment1.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('python assignment1.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inf = arg
        elif opt in ("-o", "--ofile"):
            outf = arg

    return inf, outf

def  read_csv_to_dict(inf):
    data = []
    with open(inf, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(dict(row))
    return data

def  transform_func(indata):
    data = []

    inProj = Proj(init='epsg:3301')
    outProj = Proj(init='epsg:4326')
    for elem in indata:
        t_long, t_lat = transform(inProj, outProj, elem['LEST_Y'], elem['LEST_X'])
        data.append({'LONG': t_long, 'LAT': t_lat})
    return data

'''
Stores output transformed data list to 
output file in csv format
'''
def  store_result_to_csv(outdata, outf):
    csv_columns = ['LAT', 'LONG']
    with open(outf, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in outdata:
            writer.writerow({'LAT': data['LAT'], 'LONG': data['LONG']})

if __name__ == "__main__":
    infile = ''
    outfile = ''
    infile, outfile = get_input_output_file(sys.argv[1:])

    if infile == "" or outfile == "":
        print("Empty input or output file")
        sys.exit()
    indata = []
    outdata = []
    # Read csv  input file into python dict
    indata = read_csv_to_dict(infile)

    # Transform data and store result output dict
    outdata = transform_func(indata)

    # Store result into output file in csv format
    store_result_to_csv(outdata, outfile)
