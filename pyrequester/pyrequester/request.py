# -*- coding: utf-8 -*-

"""

@author: Shuai Yuan
@date: 20/03/2015
"""
import json
from uuid import uuid4

import requests


REQ = {
    'id': str(uuid4()).replace('-', ''),
    'imp': [
        {
            'id': str(uuid4()).replace('-', ''),
            'banner': {
                'h': 250,
                'w': 300,
                'pos': 0
            },
            'bidfloor': 0.
        }
    ],
    'site': {
        'id': '102855',
        'domain': 'http://www.foobar.com',
        'cat': 'IAB3-1',
        'page': 'http://www.foobar.com/1234.html ',
        'publisher': {
            'id': '8953',
            'name': 'foobar.com',
            'cat': 'IAB3-1',
            'domain': 'foobar.com'
        }
    },
    'device': {
        'ua': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13 (KHTML, likeGecko) Version/5.1.7 Safari/534.57.2',
        'ip': '123.145.167.*'
    },
    'user': {
        'id': str(uuid4()).replace('-', '')
    },
    'at': 1,
    'cur': ['USD'],
}


def get_random_bid_request():
    req = REQ.copy()

    return req


def send_request(req, endpoint):
    resp = requests.post(endpoint, data={
        'req': json.dumps(req)
    })

    return resp.json()
