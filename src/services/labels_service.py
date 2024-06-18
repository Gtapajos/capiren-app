import requests
import json

class LabelsService():
    def get_labels(self, text, category):
        url = 'http://127.0.0.1:5000/labels'
        body = {"text": text, "category": category, "model": 'bert-base-multilingual-cased'}

        try:
            response = requests.get(url, json=body, headers={'Content-Type': 'application/json'})
            response = json.loads(response.content.decode('utf-8'))
            return response
        except Exception as e:
            print(e)
            return []

