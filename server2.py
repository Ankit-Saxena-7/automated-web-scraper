from fastapi import FastAPI
from scrape import Run as ScrapeRunner
from logger import TriggerLogSave

vApplication = FastAPI()

@vApplication.get("/")
def hello_world():
    return {"hello": "world"}


@vApplication.post("/box-office-mojo-scrapper")
def BoxOfficeScrapperView():
    TriggerLogSave()
    ScrapeRunner()
    return {"scrape": [1, 2, 3]}

# Launch server: uvicorn server2:vApplication