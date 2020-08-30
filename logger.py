import os
import datetime

BASE_DIR = os.path.dirname(__file__)

LOG_DIR = os.path.join(BASE_DIR, "logs")

os.makedirs(LOG_DIR, exist_ok=True)

def TriggerLogSave():
    vFilename = f'{datetime.datetime.now()}.txt'
    vFilepath = os.path.join(LOG_DIR, vFilename)
    with open(vFilepath, 'w+') as vFile:
        vFile.write("Scrapper executed successfully")