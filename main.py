# This only exists for creating the single-executable binary.

from server import api
import uvicorn

if __name__ == "__main__":
    uvicorn.run(api)
