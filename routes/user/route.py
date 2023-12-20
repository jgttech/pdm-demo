from app import api
from pydantic import BaseModel

class User(BaseModel):
    first_name: str
    last_name: str

@api.post("/user")
async def post_user():
    print("Hello world!!!")
    return {}
