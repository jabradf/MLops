# demonstrate arguments passed in through the command line using a modified jformat.py file

import os
import sys
import json
import argparse

def formatter(string, sort_keys=True, indent=4):
    # load incoming string into JSON
    loaded_json = json.loads(string)
    # dump as string 
    return json.dumps(loaded_json, sort_keys=sort_keys, indent=indent)

def main(path, no_sort):
    if no_sort:
        sort_keys = False
    else:
        sort_keys = True
    with open(path, 'r') as _f:
        print(
            formatter(_f.read(), sort_keys=sort_keys)
        )

#print(sys.argv)

if __name__ == '__main__':
    # implement help functionality
    parser = argparse.ArgumentParser(description="This is a jformat tool.")
    parser.add_argument("--sort", action="store_true", help="Set a sorting flag")
    args = parser.parse_args()
    print(args.sort)

    #main(sys.argv[-1], no_sort=False)  # only take the last argument
    