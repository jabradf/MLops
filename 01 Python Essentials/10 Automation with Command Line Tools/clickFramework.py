import json
import click

def formatter(string, sort_keys=True, indent=4):
    # load incoming string into JSON
    loaded_json = json.loads(string)
    # dump as string 
    return json.dumps(loaded_json, sort_keys=sort_keys, indent=indent)

# Create some decorators using click module, which eliminates the need to pass sys.argv[-1]
# The extra item, type, checks for the existence of the file given in the arguments!
@click.command()
@click.argument('path', type=click.Path(exists=True)) # check the file exists
@click.option('--sort', '-s', is_flag=True)  # add a sort flag input. Aliases can be added by adding more strings.
#is_flag sets a default option. The flag must be before the path in this instance (clickFramework.py --sort example.json)
def main(path, sort):
    with open(path, 'r') as _f:
        print(
            formatter(_f.read(), sort_keys=sort)
        )

#print(sys.argv)

if __name__ == '__main__':
    main()