import os
import sys
import json

def formatter(string, sort_keys=True, indent=4):
    # load incoming string into JSON
    loaded_json = json.loads(string)
    # dump as string 
    return json.dumps(loaded_json, sort_keys=sort_keys, indent=indent)

def main(path):
    with open(path, 'r') as _f:
        print(
            formatter(_f.read())
        )

#print(sys.argv)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        # only run if argument/s given
        main(sys.argv[-1])  # only take the last argument
    else:
        print("Please run with at least one argument.")
        print("example: python jformat.py example.json")