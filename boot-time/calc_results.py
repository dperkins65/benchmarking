#!/usr/bin/python
"""
Simple script that parses boot time timestamp files 
and saves them to a CSV output file.

Requires a directory to parse and a path to an output file.
"""

import os
import csv
import argparse
from datetime import datetime


def list_data_files(directory):
    directory = os.path.abspath(directory)
    data_files = [file for file in os.listdir(directory)]
    master_index = data_files.index('MASTER.log')
    del data_files[master_index]
    print "Found '%s' data files" % len(data_files)
    return data_files

def get_master_timestamp(directory):
    directory = os.path.abspath(directory)
    f = open(directory + '/MASTER.log', 'r')
    timestamp = f.read().strip()
    return timestamp

def get_timestamp_deltas(directory, data_files, master_timestamp):
    data = []
    print "Parsing timestamp data"
    for file in data_files:
        f = open(directory + '/' + file)
        timestamp = f.read().strip()
        master_datetime = datetime.strptime(master_timestamp, "%Y-%m-%d %H:%M:%S.%f")
        timestamp_datetime = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")
        data.append({'Desktop Name': file, 'Boot Time (s)': (timestamp_datetime - master_datetime).total_seconds()}) 
    return data

def save_to_csv(keys, data, output):
    output = os.path.abspath(output)
    print "Writing to file '%s'" % output
    f = open(output, 'wb')
    writer = csv.DictWriter(f, keys)
    writer.writer.writerow(keys)
    writer.writerows(data)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d','--directory', action='store', 
                        help='Path to the directory containing boot timestamp files', 
                        required=True)
    parser.add_argument('-o','--output', action='store', 
                        help='Path to the csv output file', 
                        required=True)
    args = vars(parser.parse_args())
    
    directory = args['directory']
    data_files = list_data_files(directory)
    master_timestamp = get_master_timestamp(directory)
    data = get_timestamp_deltas(directory, data_files, master_timestamp)
    
    keys = ['Desktop Name', 'Boot Time (s)']
    save_to_csv(keys, data, args['output'])    
