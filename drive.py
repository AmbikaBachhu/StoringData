import json
import requests
headers = {"Authorization": "Bearer ya29.a0AfH6SMDicMcor5qmBnaTFo_2BLOlxRIPcGTaLjKUGK2wkXQJjTFvglgUzD107dxZDK842EbrizbsrsEvT0SnlXpX1axbnu-9zHgizrfMeQBOHLpS_qUnk5bkSgPVwwS18Oo_da-5ZK4XHRdoQOTr8uKpJdJ7aTWJYZ0"}
para = {
    "name": "sample.png",
    "parents":["1JbIdSS_ThYAwVANCdjTtYKIrs6LR9XN_"]
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': open("./car.png", "rb")
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
print(r.text)

