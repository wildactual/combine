#!/usr/bin/python3

import argparse
from json import loads, load
import re
from os import path
from sys import exit

json_list = []


# Extract IP from string
def get_ip(line):
    regex = r"(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
    match = re.findall(regex, line)
    if len(match) != 0:
        return match[0]
    else:
        return None

# Extract Domain from string
def get_domain(str):
    regex = r"((\w+)\.)+([a-zA-Z]){2,6}"
    match = re.search(regex, str)
    if match != None:
        return match[0]
    else:
        return None

# Extract ip or domain
def get_address(line):
    match = get_ip(line)
    if not match:
        match = get_domain(line)
        if not match:
            return None
        else:
            return match
    else:
        return match    

# Check if file exists
def check_path(file_path):
    if path.isfile(file_path):
        return file_path
    else:
        print(f'{file_path} does not exist or is a directory')
        exit(1)
        
def make_json_lst(file):
    file_path = check_path(file)
    try:
        file =  open(file_path, 'r')
        line = json.load(file.readline())
        json_list.append()(line)
    except:
        print(f'Could not read in {file}')
    finally:
        file.close()


if __name__ == '__main__':
    
    json_dict = {}
    
    parser = argparse.ArgumentParser(
        description='Combine files')
    parser.add_argument(
        '-j',
        '--json',
        help='Json file',
        required=True)
    parser.add_argument(
        '-f',
        '--file',
        help='text file',
        required=True)
    parser.add_argument(
        '-o',
        '--out_file',
        help='file destination of output',
        default=False)
    args = parser.parse_args()
    
    check_path(args.file)
    json_dict = json.loads(check_path(args.json))
    
    if args.out_file != False:
        try:
            with open(args.out_file, 'w+') as write:
                pass
        except:
            pass
    if args.out_file == False:
        print('test')
            
    print(args)
