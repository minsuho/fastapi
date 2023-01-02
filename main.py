from fastapi import FastAPI
from youtubesearchpython import VideosSearch, Video, ResultMode

app = FastAPI()

@app.get("/")
async def root():
    return {}

@app.get("/VideosSearch/")
async def VideosSearch1(q: str = None, n: int = 1):
    videosSearch = VideosSearch(q, limit = n, region = 'KO')
    data = videosSearch.result()
    return data

@app.get("/videofullInfo/")
async def videofullInfo(id: str = None):
    video = Video.get(id, mode = ResultMode.json, get_upload_date=True)
    return video

@app.get("/videoInfo/")
async def videoInfo(id: str = None):
    video = Video.getInfo(id, mode = ResultMode.json)
    return video
