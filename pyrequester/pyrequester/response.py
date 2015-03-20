# -*- coding: utf-8 -*-

"""

@author: Shuai Yuan
@date: 20/03/2015
"""
import json
from random import random, seed

seed()

BID = {
    'id': '',
    'impid': '',
    'price': 0.,
    'adid': '314',
    'nurl': 'http://localhost:8081/win_notice/',
    'adm': '',
    'adomain': [
        'advertiser.domain.com'
    ],
    'iurl': 'http://adserver.com/path/to/sample/image',
    'cid': 'campaign111',
    'crid': 'creative112',
    'attr': []
}

REPS = {
    'id': '1234567890',
    'seatbid': [
        {
            'bid': [

            ],
            'seat': '512'
        }
    ],
    'bidid': 'abc1123',
    'cur': 'USD'
}


def get_random_bid_response(req):
    req = json.loads(req)

    resp = REPS.copy()

    count = 0
    for imp in req['imp']:
        imp_id = imp['id']

        bid = BID.copy()
        bid['id'] = str(count)
        bid['price'] = random()
        bid['impid'] = imp_id
        bid['nurl'] += imp_id

        resp['seatbid'][0]['bid'].append(bid)

        count += 1

    return resp


def send_response(resp, endpoint):
    pass