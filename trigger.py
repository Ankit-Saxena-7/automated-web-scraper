import requests

vNgrokURL = "https://7f95a09da216.ngrok.io"

vEndpoint = f'{vNgrokURL}/box-office-mojo-scrapper'

vRequest = requests.post(vEndpoint, json={})

print('successful')