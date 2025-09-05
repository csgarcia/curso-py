from pathlib import Path

path = Path("routes")
# path.exists()  # False, directory does not exist
# path.mkdir()  # Create the directory
# path.rmdir()  # Remove the directory
# path.rename("new_folder")  # Rename the directory

# for p in path.iterdir():  # Iterator of files in the directory
#     print(p) # routes/01-path.py, routes/02-directories.py

files = [ p for p in path.iterdir() if not p.is_dir() ]


# use glob to filter files by pattern
py_files = [ p for p in path.glob("*.py") if not p.is_dir() ]
print(py_files)  # [PosixPath('routes/01-path.py'), PosixPath('routes/02-directories.py')]

# All files with extendion py
all_py_files = [ p for p in path.rglob("**/*.py") ]
print(all_py_files)  # [PosixPath('routes/01-path.py'), PosixPath('routes/02-directories.py')]