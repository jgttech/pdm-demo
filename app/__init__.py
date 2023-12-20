from pathlib import Path
from fastapi import FastAPI
from app import routes

# Gets the path of this file without
# the .py ext as the app invocation path.
API_PATH = Path(__file__).stem

# FastAPI instance.
api = FastAPI(title="DAS API")

# Loads the routes dynamically from the "routes" directory.
# For the routes to work, you need to do this AFTER the
# FastAPI instance has been instantiated.
routes.load()
