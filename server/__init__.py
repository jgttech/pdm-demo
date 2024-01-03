from pathlib import Path
from fastapi import FastAPI

# Gets the path of this file without
# the .py ext as the app invocation path.
API_PATH = Path(__file__).stem

# FastAPI instance.
api = FastAPI(title="DAS API")

from routes import *
