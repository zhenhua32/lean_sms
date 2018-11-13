# -*- coding: utf-8 -*-

import os

import leancloud
from gevent import monkey

from app.app import app
from cloud_func.cloud import engine
from cloud_func.cloud_env import APP_ID, APP_KEY, MASTER_KEY, PORT

monkey.patch_all()

leancloud.init(APP_ID, app_key=APP_KEY, master_key=MASTER_KEY)
# 如果需要使用 master key 权限访问 LeanCLoud 服务，请将这里设置为 True
leancloud.use_master_key(True)

# 需要重定向到 HTTPS 可去除下一行的注释。
# app = leancloud.HttpsRedirectMiddleware(app)
app = engine.wrap(app)
application = app

if __name__ == '__main__':
  # 只在本地开发环境执行的代码
  from gevent.pywsgi import WSGIServer
  from geventwebsocket.handler import WebSocketHandler
  from werkzeug.serving import run_with_reloader
  from werkzeug.debug import DebuggedApplication

  @run_with_reloader
  def run():
    global application
    app.debug = True
    application = DebuggedApplication(application, evalex=True)
    server = WSGIServer(('localhost', PORT), application, handler_class=WebSocketHandler)
    server.serve_forever()

  run()
