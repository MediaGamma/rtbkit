# -*- coding: utf-8 -*-

"""

@author: Shuai Yuan
@date: 20/03/2015
"""

import json

from flask import Flask

from request import get_random_bid_request, send_request

SECRET_KEY = '\\\xc1\xbc\x1a\xbe\n\x87:T\xbby+\x9an\xdc}\xfe\xf4\xe2x('

app = Flask(__name__)


@app.route('/random_bid_request/')
def random_bid_request():
    req = get_random_bid_request()

    resp = send_request(req, 'http://localhost:8081/random_bid_response/')

    req = json.dumps(req, indent=4)
    resp = json.dumps(resp, indent=4)

    return req + '\n' + resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082, debug=True)

