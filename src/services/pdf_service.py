import requests
import json

class PdfService():
    def get_text(self, file):
        url = 'http://127.0.0.1:5000/pdf_text'
        files = {'file': (file.name, file, 'application/pdf')}

        try:
            response = requests.get(url, files=files)
            response = json.loads(response.content.decode('utf-8'))
            return response
        except Exception as e:
            print(e)
            return []