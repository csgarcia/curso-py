# doing this the dependency is installed globally and not in a virtual environment
# with virtual environments is a better practice because it avoids dependency conflicts

# to create a virtual environment:
# python -m venv venv
# to activate it:
# on Windows: .\venv\Scripts\activate
# on MacOS/Linux: source env/bin/activate
# to disable it: deactivate

# there is another way to manage dependencies: pipenv
# to install it: pip3 install pipenv

import requests

r = requests.get("https://google.com")
print(r.status_code)
