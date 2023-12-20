# This only exists for creating the single-executable binary.

from app import api
import uvicorn

if __name__ == "__main__":
    uvicorn.run(api)
