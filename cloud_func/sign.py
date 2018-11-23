import hashlib
import hmac
import os
import random
import secrets
import time

from leancloud import Engine, LeanEngineError

from cloud_func.cloud_env import APP_ID, MASTER_KEY
"""
实现签名
https://leancloud.cn/docs/realtime_v2.html#hash-188224612
"""

engine = Engine()


def get_signature(text, timestamp, nonce):
  signature = hmac.new(MASTER_KEY.encode('utf-8'), text.encode('utf-8'), hashlib.sha1).hexdigest()
  data = {'signature': signature, 'timestamp': timestamp, 'nonce': nonce}
  return data


@engine.define
def sign_login(client_id, **args):
  """
  用户登录的签名
  """
  timestamp = int(time.time() * 1000)
  nonce = secrets.token_hex(6)
  text = f'{APP_ID}:{client_id}::{timestamp}:{nonce}'
  data = get_signature(text, timestamp, nonce)
  return data


@engine.define
def sign_chat(client_id, member_ids, **args):
  """
  对话签名
  """
  timestamp = int(time.time() * 1000)
  nonce = secrets.token_hex(6)
  member_ids.sort()
  text = f'{APP_ID}:{client_id}:{":".join(member_ids)}:{timestamp}:{nonce}'
  data = get_signature(text, timestamp, nonce)
  return data


@engine.define
def sign_group(client_id, conv_id, member_ids, action, **args):
  """
  群组功能的签名, action in ['invite', 'kick']
  """
  timestamp = int(time.time() * 1000)
  nonce = secrets.token_hex(6)
  member_ids.sort()
  text = f'{APP_ID}:{client_id}:{conv_id}:{":".join(member_ids)}:{timestamp}:{nonce}:{action}'
  data = get_signature(text, timestamp, nonce)
  return data


@engine.define
def sign_chat_history(client_id, conv_id, **args):
  """
  查询聊天记录的签名
  """
  signature_ts = int(time.time())
  nonce = secrets.token_hex(6)
  text = f'{APP_ID}:{client_id}:{conv_id}:{nonce}:{signature_ts}'

  signature = hmac.new(MASTER_KEY.encode('utf-8'), text.encode('utf-8'), hashlib.sha1).hexdigest()
  data = {'signature': signature, 'signature_ts': signature_ts, 'nonce': nonce}
  return data


@engine.define
def sign_block(client_id, conv_id, action, member_ids=None, **args):
  """
  黑名单的签名
  """
  timestamp = int(time.time() * 1000)
  nonce = secrets.token_hex(6)
  if member_ids:
    member_ids.sort()
    text = f'{APP_ID}:{client_id}:{conv_id}:{":".join(member_ids)}:{timestamp}:{nonce}:{action}'
  else:
    text = f'{APP_ID}:{client_id}:{conv_id}::{timestamp}:{nonce}:{action}'

  data = get_signature(text, timestamp, nonce)
  return data
