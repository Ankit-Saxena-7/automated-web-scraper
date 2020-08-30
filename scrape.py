import os
import datetime
import requests
import pandas as pd
from requests_html import HTML

BASE_DIR = os.path.dirname(__file__)

def URLToText(pURL, pFileName="world.html", pSave=False):
    vRequest = requests.get(pURL)
    if vRequest.status_code == 200:
        vHTMLText = vRequest.text
        if pSave:
            with open(pFileName, 'w') as vFile:
                vFile.write(vHTMLText)
        return vHTMLText
    return None

def ParseAndExtract(pURL, pName='2020'):
    vHTMLText = URLToText(pURL)
    print("HTML: " + vHTMLText)
    if vHTMLText == None:
        return False
    vHTML = HTML(html=vHTMLText)
    vTableClass = ".imdb-scroll-table"
    vTable = vHTML.find(vTableClass)

    vTableData = []
    vTableDataDicts = []
    vHeaderNames = []
    if len(vTable) == 0:
        return False
    vParsedTable = vTable[0]
    vRows = vParsedTable.find("tr")
    vHeaderRow = vRows[0]
    vHeaderCols = vHeaderRow.find('th')
    vHeaderNames = [vCol.text for vCol in vHeaderCols]
    for vRow in vRows[1:]:
        # print(vRow.text)
        vCols = vRow.find("td")
        vRowData = []
        vRowDictData = {}
        for vIndex, vCol in enumerate(vCols):
            # print(vIndex, vCol.text, '\n\n')
            vHeaderName = vHeaderNames[vIndex]
            vRowDictData[vHeaderName] = vCol.text
            vRowData.append(vCol.text)
        vTableDataDicts.append(vRowDictData)
        vTableData.append(vRowData)
    vDataFrame = pd.DataFrame(vTableData, columns=vHeaderNames)
    vPath = os.path.join(BASE_DIR, 'data')
    os.makedirs(vPath, exist_ok=True)
    vFilepath = os.path.join('data', f'{pName}.csv')
    vDataFrame.to_csv(vFilepath, index=False)
    return True

def Run(pStartYear=None, pYearsAgo=0):
    print("Started Run")
    if pStartYear == None:
        vNow = datetime.datetime.now()
        pStartYear = vNow.year
    assert isinstance(pStartYear, int)
    assert isinstance(pYearsAgo, int)
    assert len(f"{pStartYear}") == 4
    for vCounter in range(0, pYearsAgo+1):
        vURL = f"https://www.boxofficemojo.com/year/world/{pStartYear}/"
        vFinished = ParseAndExtract(vURL, pName=pStartYear)
        if vFinished:
            print(f"Finished {pStartYear}")
        else:
            print(f"{pStartYear} not finished")
        pStartYear -= 1