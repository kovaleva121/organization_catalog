from fastapi import Header, HTTPException

from .config import settings


def api_key_auth(x_api_key: str = Header(...)):
    if x_api_key != settings.API_KEY:
        raise HTTPException(status_code=403, detail='Invalid API key')
    return x_api_key
