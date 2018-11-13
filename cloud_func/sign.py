import hashlib
import hmac
import os
import random
import secrets
import time

from leancloud import Engine, LeanEngineError

from cloud_env import APP_ID, MASTER_KEY

"""
实现签名
https://leancloud.cn/docs/realtime_v2.html#hash-188224612
"""

engine = Engine()


def get_signature(text, timestamp, none):
  signature = hmac.new(MASTER_KEY.encode('utf-8'), text.encode('utf-8'), hashlib.sha1).hexdigest()
  data = {'signature': signature, 'timestamp': timestamp, 'none': none}
  return data


@engine.define
def sign_login(client_id, **args):
  """
  用户登录的签名
  """
  timestamp = str(int(time.time() * 1000))
  none = secrets.token_hex(6)
  text = f'{APP_ID}:{client_id}::{timestamp}:{none}'
  data = get_signature(text, timestamp, none)
  return data


@engine.define
def sign_chat(client_id, member_ids, **args):
  """
  对话签名
  """
  timestamp = str(int(time.time() * 1000))
  none = secrets.token_hex(6)
  member_ids.sort()
  text = f'{APP_ID}:{client_id}:{":".join(member_ids)}:{timestamp}:{none}'
  data = get_signature(text, timestamp, none)
  return data


@engine.define
def sign_group(client_id, conv_id, member_ids, action, **args):
  """
  群组功能的签名, action in ['invite', 'kick']
  """
  timestamp = str(int(time.time() * 1000))
  none = secrets.token_hex(6)
  member_ids.sort()
  text = f'{APP_ID}:{client_id}:{conv_id}:{":".join(member_ids)}:{timestamp}:{none}:{action}'
  data = get_signature(text, timestamp, none)
  return data


@engine.define
def sign_chat_history(client_id, conv_id):
  """
  查询聊天记录的签名
  """
  timestamp = str(int(time.time() * 1000))
  none = secrets.token_hex(6)
  signature_ts = str(int(time.time()))
  none = secrets.token_hex(6)
  text = f'{APP_ID}:{client_id}:{conv_id}:{none}:{signature_ts}'

  signature = hmac.new(MASTER_KEY.encode('utf-8'), text.encode('utf-8'), hashlib.sha1).hexdigest()
  data = {'signature': signature, 'signature_ts': signature_ts, 'none': none}
  return data


@engine.define
def sign_block(client_id, conv_id, action, member_ids=None, **args):
  """
  黑名单的签名
  """
  timestamp = str(int(time.time() * 1000))
  none = secrets.token_hex(6)
  if member_ids:
    member_ids.sort()
    text = f'{APP_ID}:{client_id}:{conv_id}:{":".join(member_ids)}:{timestamp}:{none}:{action}'
  else:
    text = f'{APP_ID}:{client_id}:{conv_id}::{timestamp}:{none}:{action}'

  data = get_signature(text, timestamp, none)
  return data
