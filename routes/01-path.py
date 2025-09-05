# Path is used for filesystem paths manipulation
from pathlib import Path

# For windows paths, use:
# Path(r"C:\temp\some_folder")  # Raw string to avoid escaping backslashes

# Path("/usr/bin")  # Unix-style path
# Path()
# Path.home()  # User's home directory
# Path('one/__init__.py')


path = Path("hellow-world/my_file.py")
path.is_file()  # False, file does not exist
path.is_dir()  # False, directory does not exist
path.exists()  # False, path does not exist

print(
    path,
    path.name,  # my_file.py
    path.suffix,  # .py
    path.stem,  # my_file
    path.parent,  # hellow-world
    path.absolute(),  # /full/path/to/hellow-world/my_file.py
    path.parts,  # ('hellow-world', 'my_file.py')
)

p = path.with_name("new_file.txt")  # hellow-world/new_file.txt
print(p)
p = path.with_suffix(".bat")  # hellow-world/my_file.bat
print(p)
p = path.with_stem("new_file")  # hellow-world/new_file.py
print(p)