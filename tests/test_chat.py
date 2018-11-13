import os
import sys

import leancloud
from dotenv import load_dotenv
from leancloud import cloudfunc
"""
Conversation 的示例
"""

load_dotenv()

APP_ID = os.getenv('APP_ID')
APP_KEY = os.getenv('APP_KEY')
TOBE_PASS = os.getenv('TOBE_PASS')
TOBE_PHONE = os.getenv('TOBE_PHONE')
TOBE_EMAIL = os.getenv('TOBE_EMAIL')

leancloud.init(APP_ID, app_key=APP_KEY)

user = leancloud.User()
user.login('tobe', TOBE_PASS)
print(user.get_roles()[0].get('name'))

role_query = leancloud.Query(leancloud.Role)
role_query.equal_to('name', 'admin')
role_query_list = role_query.find()
print(role_query_list)
admin  = role_query_list[0]
user_relation = admin.relation('users')
users_with_admin = user_relation.query.find()[0]
print(users_with_admin.get('objectId'))
print(users_with_admin.id)


role_query.equal_to('users', leancloud.User.get_current())
role_query_with_current_user = role_query.find()
print(role_query_with_current_user)

admin = leancloud.Role('admin')
relation = admin.get_users()
relation.add(leancloud.User.get_current())

# admin.save()


def create_user():
  user = leancloud.User()
  user.set_username('tobe')
  user.set_mobile_phone_number(TOBE_PHONE)
  user.set_email(TOBE_EMAIL)
  user.set_password(TOBE_PASS)
  user.sign_up()


def create():
  conversation = leancloud.Conversation()
  conversation.set('name', 'hello')
  print(conversation.name)
  conversation.save()
  print(conversation)



if __name__ == '__main__':
  pass