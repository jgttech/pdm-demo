from app import api
from typing import Union

@api.get("/name/{first_name}")
async def get_name(first_name: str, last_name: Union[str, None]):
    return {
        "First Name": first_name,
        "Last Name": last_name
    }
