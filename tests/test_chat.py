import os
import sys

import leancloud
import requests
from dotenv import load_dotenv
from leancloud import cloudfunc
"""
Conversation 的示例
"""

load_dotenv()

APP_ID = os.getenv('APP_ID')
APP_KEY = os.getenv('APP_KEY')
MASTER_KEY = os.getenv('MASTER_KEY')
TOBE_PASS = os.getenv('TOBE_PASS')
TOBE_PHONE = os.getenv('TOBE_PHONE')
TOBE_EMAIL = os.getenv('TOBE_EMAIL')

leancloud.init(APP_ID, app_key=APP_KEY, master_key=MASTER_KEY)

# user = leancloud.User()
# user.login('tobe', TOBE_PASS)

# headers = {'X-LC-Id': APP_ID, 'X-LC-Key': APP_KEY}
# url = 'https://vcliyymf.api.lncld.net/1.2/rtm/clients/sign'
# params = {'session_token': user.session_token}
# r = requests.get(url, params=params, headers=headers)
# print(r.status_code)
# print(r.json())

# role_query = leancloud.Query(leancloud.Role)
# role_query.equal_to('name', 'admin')
# role_query_list = role_query.find()
# print(role_query_list)
# admin = role_query_list[0]
# user_relation = admin.relation('users')
# users_with_admin = user_relation.query.find()[0]
# print(users_with_admin.get('objectId'))
# print(users_with_admin.id)

# role_query.equal_to('users', leancloud.User.get_current())
# role_query_with_current_user = role_query.find()
# print(role_query_with_current_user)

# admin = leancloud.Role('admin')
# relation = admin.get_users()
# relation.add(leancloud.User.get_current())
# admin.save()


def create_user():
  user = leancloud.User()
  user.set_username('tobe')
  user.set_mobile_phone_number(TOBE_PHONE)
  user.set_email(TOBE_EMAIL)
  user.set_password(TOBE_PASS)
  user.sign_up()


def create_conversation():
  conversation = leancloud.Conversation()
  conversation.set('name', 'hello')
  conversation.set('unique', True)
  conversation.add_member('cat')
  conversation.add_member('dog')

  # acl = leancloud.ACL()
  # acl.set_public_read_access(True)
  # acl.set_public_write_access(True)
  # print(acl.dump())
  # conversation.set_acl(acl)
  conversation.save()
  print(conversation.id)
  # 5beb8498fb4ffe006bbc6ff2


def find_conversation():
  conversation = leancloud.Conversation.query.get('5beb903860d9007f7ba8423f')
  print(conversation.members)
  acl = leancloud.ACL()
  acl.set_public_read_access(True)
  print(acl.dump())
  conversation.set_acl(acl)
  conversation.save()


if __name__ == '__main__':
  find_conversation()