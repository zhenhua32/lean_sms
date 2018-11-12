# coding: utf-8
import time
import random
import os
import hashlib
import hmac
from leancloud import Engine
from leancloud import LeanEngineError

engine = Engine()
APP_ID = os.environ['LEANCLOUD_APP_ID']
APP_KEY = os.environ['LEANCLOUD_APP_KEY']
MASTER_KEY = os.environ['LEANCLOUD_APP_MASTER_KEY']
PORT = int(os.environ['LEANCLOUD_APP_PORT'])


@engine.define
def hello(**params):
    if 'name' in params:
        return 'Hello, {}!'.format(params['name'])
    else:
        return 'Hello, LeanCloud!'


@engine.define
def sign(client_id, **params):
    timestamp = str(int(time.time() * 1000))
    none = ''
    text = f'{APP_ID}:{client_id}::{timestamp}:{none}'

    data = {
        'timestamp': timestamp,
        'none': none
    }
    return {}
