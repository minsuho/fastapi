from fastapi import FastAPI
from youtubesearchpython import VideosSearch, Video, ResultMode
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/")
async def root():
    return {}

@app.get("/youtube/VideosSearch/")
async def VideosSearch1(q: str = None, n: int = 1):
    videosSearch = VideosSearch(q, limit = n, region = 'KO')
    data = videosSearch.result()
    return data

@app.get("/youtube/videofullInfo/")
async def videofullInfo(id: str = None):
    video = Video.get(id, mode = ResultMode.json, get_upload_date=True)
    return video

@app.get("/youtube/videoInfo/")
async def videoInfo(id: str = None):
    video = Video.getInfo(id, mode = ResultMode.json)
    return video
@app.get("/kleague")
async def kleague(y: str = None):
    # y = "2023"
    if y >= 2023:
        req = requests.get(f'https://sports.news.naver.com/kfootball/record/index?category=kleague&year={y}').text
        html = BeautifulSoup(req, 'html.parser')
        t1 = html.select_one('#regularGroup_table')
        t = t1.select('tr')
        data = []
        for i in t:
            data.append({
                '팀이름':i.select_one('td:nth-child(2)').text.strip(),
                '경기수':i.select_one('td:nth-child(3)').text,
                '승점':i.select_one('td:nth-child(4)').text,
                '승':i.select_one('td:nth-child(5)').text,
                '무':i.select_one('td:nth-child(6)').text,
                '패':i.select_one('td:nth-child(7)').text,
                '득점':i.select_one('td:nth-child(8)').text,
                '실점':i.select_one('td:nth-child(9)').text,
                '득실차':i.select_one('td:nth-child(10)').text,
                '도움':i.select_one('td:nth-child(11)').text,
                '파올':i.select_one('td:nth-child(12)').text,

            })
            # print(i.select_one('td:nth-child(2)').text.strip())
            # print(i.select_one('td:nth-child(3)').text)
            # print(i.select_one('td:nth-child(4)').text)
            # print(i.select_one('td:nth-child(5)').text)
            # print(i.select_one('td:nth-child(6)').text)
            # print(i.select_one('td:nth-child(7)').text)
            # print(i.select_one('td:nth-child(8)').text)
            # print(i.select_one('td:nth-child(9)').text)
            # print(i.select_one('td:nth-child(10)').text)
            # print(i.select_one('td:nth-child(11)').text)
            # print(i.select_one('td:nth-child(12)').text)
    elif y < 2023:
        req = requests.get(f'https://sports.news.naver.com/kfootball/record/index?category=kleague&year={y}').text
        html = BeautifulSoup(req, 'html.parser')
        t1 = html.select_one('#splitGroupA_table')
        t = t1.select('tr')
        li = []
        for i in t:
            li.append({
                '팀이름':i.select_one('td:nth-child(2)').text.strip(),
                '경기수':i.select_one('td:nth-child(3)').text,
                '승점':i.select_one('td:nth-child(4)').text,
                '승':i.select_one('td:nth-child(5)').text,
                '무':i.select_one('td:nth-child(6)').text,
                '패':i.select_one('td:nth-child(7)').text,
                '득점':i.select_one('td:nth-child(8)').text,
                '실점':i.select_one('td:nth-child(9)').text,
                '득실차':i.select_one('td:nth-child(10)').text,
                '도움':i.select_one('td:nth-child(11)').text,
                '파올':i.select_one('td:nth-child(12)').text,})
            
        t1 = html.select_one('#splitGroupB_table')
        t = t1.select('tr')
        li1 = []
        for i in t:
            li1.append({
                '팀이름':i.select_one('td:nth-child(2)').text.strip(),
                '경기수':i.select_one('td:nth-child(3)').text,
                '승점':i.select_one('td:nth-child(4)').text,
                '승':i.select_one('td:nth-child(5)').text,
                '무':i.select_one('td:nth-child(6)').text,
                '패':i.select_one('td:nth-child(7)').text,
                '득점':i.select_one('td:nth-child(8)').text,
                '실점':i.select_one('td:nth-child(9)').text,
                '득실차':i.select_one('td:nth-child(10)').text,
                '도움':i.select_one('td:nth-child(11)').text,
                '파올':i.select_one('td:nth-child(12)').text,})
        data = {"A":li, "B":li1}

    return data


@app.get("/kleague2")
async def kleague2(y: str = None):
    # y = "2023"
    req = requests.get(f'https://sports.news.naver.com/kfootball/record/index?category=kleague&year={y}').text
    html = BeautifulSoup(req, 'html.parser')
    t1 = html.select_one('#regularGroup_table')
    t = t1.select('tr')
    data = []
    for i in t:
        data.append({
            '팀이름':i.select_one('td:nth-child(2)').text.strip(),
            '경기수':i.select_one('td:nth-child(3)').text,
            '승점':i.select_one('td:nth-child(4)').text,
            '승':i.select_one('td:nth-child(5)').text,
            '무':i.select_one('td:nth-child(6)').text,
            '패':i.select_one('td:nth-child(7)').text,
            '득점':i.select_one('td:nth-child(8)').text,
            '실점':i.select_one('td:nth-child(9)').text,
            '득실차':i.select_one('td:nth-child(10)').text,
            '도움':i.select_one('td:nth-child(11)').text,
            '파올':i.select_one('td:nth-child(12)').text,

        })
    return data
