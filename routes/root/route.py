from app import api

@api.get("/")
async def get_root():
    return {
        "Hello": "World"
    }
