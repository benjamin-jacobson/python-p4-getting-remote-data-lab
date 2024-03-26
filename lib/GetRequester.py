import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        r = requests.get(self.url)
        return r.content

    def load_json(self):
        data = self.get_response_body()
        js = json.loads(data)
        return js