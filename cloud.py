# coding: utf-8
import hashlib
import hmac
import os
import random
import time

from leancloud import Engine, LeanEngineError

from cloud_env import APP_ID

engine = Engine()


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

  data = {'timestamp': timestamp, 'none': none}
  return {}
