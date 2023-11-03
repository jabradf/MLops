import fire
from mylib.bot import scrape

'''
Python Fire is a library for automatically generating command line interfaces (CLIs) with a single line of code.

It will turn any Python module, class, object, function, etc. (any Python component will work!) into a CLI. 
It’s called Fire because when you call Fire(), it fires off your command.
'''

if __name__ == "__main__":
    fire.Fire(scrape)
