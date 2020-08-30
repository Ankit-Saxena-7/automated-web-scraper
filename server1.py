from flask import Flask
from scrape import Run as ScrapeRunner
from logger import TriggerLogSave

vApplication = Flask(__name__)

@vApplication.route("/", methods=['GET'])
def HelloWorld():
    return "Hello world, this is Flask!"

@vApplication.route("/internal-page", methods=['GET'])
def HelloUniverse():
    return "Hello world, this is another page in Flask!"

@vApplication.route("/box-office-mojo-scrapper", methods=['POST'])
def BoxOfficeScrapperView():
    TriggerLogSave()
    ScrapeRunner()
    return "Donezo"

# Launch server: gunicorn server1:vApplication