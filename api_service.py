import datetime
import json
import logging
import requests


class ApiService:
    def __init__(self, base_url, file_directory="output/"):
        self.url = base_url
        self.header = {'content-type': 'application/json'}
        self.file_directory = file_directory

    def get(self, end_point):
        try:
            response = requests.get(self.url + end_point, headers=self.header)
            response = response.json()

            # write to iso dated file
            now = datetime.datetime.now().astimezone().replace(microsecond=0).isoformat() + "_-_hot.json"
            now = self.file_directory + now.replace(":", "꞉")
            with open(now, 'w', encoding='utf-8') as f:
                json.dump(response, f, ensure_ascii=False, indent=4)
            return response
        except:
            logging.warning('API failed to fetch results')
            return []
