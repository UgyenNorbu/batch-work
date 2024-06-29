import os
import sys

from .bw_sort import bw_sort
from .bw_rename import bw_rename

def main():
    if len(sys.argv) < 2:
        print("Error: Please follow the following usage")
        print("Usage: bw_rename <prefix> <directory_path>")
        print("Usage: bw_sort <directory_path>")

    elif 'bw_sort' in sys.argv[0] and len(sys.argv) == 2:
        directory_path = sys.argv[1]
        bw_sort(directory_path)
        
    elif 'bw_rename' in sys.argv[0] and len(sys.argv) == 3:
        prefix = sys.argv[1]
        directory_path = sys.argv[2]
        bw_rename(directory_path, prefix)

    else:
        print("Error: Please follow the following usage")
        print("Usage: bw_rename <prefix> <directory_path>")
        print("Usage: bw_sort <directory_path>")

if __name__ == "__main__":
    main()