from pydantic import BaseModel

class URLCreate(BaseModel):
    url: str

class URLStats(BaseModel):
    short_id: str
    clicks: int