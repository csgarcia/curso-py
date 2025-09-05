from pathlib import Path

path = Path()

paths = [p for p in path.iterdir() if p.is_dir()]

dependencies = {
    "db": "Database connection",
    "api": "API client",
    "graphql": "GraphQL client",
}


def load(p):
    # __import__ is a built-in function to import a module by its name
    package = __import__(str(p).replace("/", "."))
    try:
        package.init(**dependencies)
    except:
        print(f"Module {p} has no init function")


list(map(load, paths))
