# examples/things.py

# Let's get this party started!
from wsgiref.simple_server import make_server

import falcon
import json

from src.tokenize import Tokenization 


app = falcon.App()

app.add_route('/tokenization', Tokenization())

if __name__ == '__main__':
    port = 8000
    with make_server('', port, app) as httpd:
        print('Port: '  + str(port))
        httpd.serve_forever()