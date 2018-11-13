import os

import leancloud
from dotenv import load_dotenv
from leancloud import cloudfunc

"""
调用云函数的示例
"""

load_dotenv()

APP_ID = os.getenv('APP_ID')
APP_KEY = os.getenv('APP_KEY')

leancloud.init(APP_ID, app_key=APP_KEY)

# 测试签名函数
data = {'client_id': 'cat'}
result = cloudfunc.run('sign_login', **data)
print(result)

data = {
  'client_id': 'cat',
  'member_ids': ['cat', 'dog', 'duck'],
}
result = cloudfunc.run('sign_chat', **data)
print(result)

data = {
  'client_id': 'cat',
  'conv_id': 'hello',
  'member_ids': ['cat', 'dog', 'duck'],
  'action': 'invite',
}
result = cloudfunc.run('sign_group', **data)
print(result)

data = {
  'client_id': 'cat',
  'conv_id': 'hello',
}
result = cloudfunc.run('sign_chat_history', **data)
print(result)

data = {
  'client_id': 'cat',
  'conv_id': 'hello',
  'member_ids': ['cat', 'dog', 'duck'],
  'action': 'client-block-conversations'
}
result = cloudfunc.run('sign_block', **data)
print(result)
print(type(result))
