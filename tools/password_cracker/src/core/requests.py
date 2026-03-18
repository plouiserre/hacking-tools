import requests

class Requests: 
    def __init__(self, url):
        self.url = url         

    def post(self, pseudonyme, password):
        param = {'Pseudonyme': pseudonyme, 'MotDePasse': password}

        req = requests.post(self.url, json = param)

        print(req.text)