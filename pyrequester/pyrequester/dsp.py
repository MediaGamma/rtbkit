# -*- coding: utf-8 -*-

"""

@author: Shuai Yuan
@date: 20/03/2015
"""

import json

from flask import Flask, request

from response import get_random_bid_response

SECRET_KEY = '\\\xc1\xbc\x1a\xbe\n\x87:T\xbby+\x9an\xdc}\xfe\xf4\xe2x('

app = Flask(__name__)


@app.route('/random_bid_response/', methods=['post'])
def random_bid_response():
    req = request.values['req']

    resp = get_random_bid_response(req)

    return json.dumps(resp)


@app.route('/win_notice/<imp_id>')
def win_notice(imp_id):

    return '%s is now an impression' % imp_id


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
