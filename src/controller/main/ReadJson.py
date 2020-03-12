import pandas as pd
import os

def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'Output.json')
    print(filename)

if __name__ == '__main__':
    main()
