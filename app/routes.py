from importlib.machinery import SourceFileLoader
from pathlib import Path
from glob import glob
from os.path import join

# [About]
# In order to support directory/file names that match
# the file path for how I like to write routes, I need
# to dynamically load the modules for each route this
# way. This because Python, as a language, does not know
# how to import from names with special characters like
# curly braces.
#
# For me, I like to use route directories and have them
# closely named after the Fast API route names where the
# slash is translated to a dot, but for the most part it
# follows the API structure. In my experience, this solution
# scales well, and creates a clear 1:1 file-to-API map
# that makes it easy for a developer to hop in and start
# writing APIs.
def load():
    routes_path = str(Path().absolute().joinpath('routes'))
    routes = glob(f"{routes_path}/*/", recursive = True)

    for idx, route in enumerate(routes):
        SourceFileLoader(f"route_{idx}", join(route, 'route.py')).load_module()
