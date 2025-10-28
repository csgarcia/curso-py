# Install dependencies — short and simple

This file shows the minimal steps to (1) create an isolated environment, (2) install packages, (3) record them in `popular-packages/requirements.txt`, and (4) run a Python file.

Replace `python3` below with `/opt/homebrew/bin/python3` if your system needs that exact binary.

1) Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
or 
source venv/bin/activate
```

2) Install a package

```bash
pip install <package-name>
```

3) Record the package in the project's requirements file

Append just the package you installed:

```bash
pip freeze | grep <package-name> >> popular-packages/requirements.txt
```

Or regenerate the entire file (captures all installed packages):

```bash
pip freeze > popular-packages/requirements.txt
```

4) Install from requirements

```bash
pip install -r popular-packages/requirements.txt
```

5) Run a Python file

With the virtualenv activated you can run a script directly:

```bash
python path/to/script.py
# example
python modules/app.py
```

If the code is in a package and you want to execute a module by name (recommended for package-aware imports):

```bash
python -m package.module
# example (run the utilities module as a module):
python -m modules.users.taxes.utilities
```

6) If `pip` is missing

```bash
python3 -m ensurepip --upgrade
# or
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```

7) Commit updated requirements

```bash
git add popular-packages/requirements.txt
git commit -m "Update dependencies"
git push
```

That's it — short and focused. If you want, I can append `twilio` or `sendgrid` (already present in `popular-packages/requirements.txt`) or regenerate that file from a venv and commit it for you.
