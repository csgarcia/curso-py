import os
from pathlib import Path
import sys

# print(sys.argv)  # list of command line arguments

# small example of pass a file and rename it


def cli(args):
    if len(args) == 1:
        print("No arguments provided")
        return

    if len(args) != 3:
        print("Usage: python script.py <source> <destination>")
        return

    source = args[1]
    source_path = Path(source)
    if not source_path.exists():
        print(f"Source file '{source}' does not exist.")
        return

    destination = args[2]
    destination_path = Path(destination)
    if destination_path.exists():
        print(f"Destination file '{destination}' already exists.")
        return

    os.rename(str(source), str(destination))
    print(f"Renamed '{source}' to '{destination}'")


cli(sys.argv)
