# coding: utf-8

from datetime import datetime

from flask import Flask, jsonify, render_template
from flask_restful import Api, Resource
from flask_sockets import Sockets

app = Flask(__name__)
api = Api(app)
sockets = Sockets(app)


class HelloWorld(Resource):
  def get(self):
    return {'hello': 'world'}


api.add_resource(HelloWorld, '/')


@app.route('/time')
def time():
  return str(datetime.now())


@sockets.route('/echo')
def echo_socket(ws):
  while True:
    message = ws.receive()
    ws.send(message)


if __name__ == '__main__':
  app.run(port=3000)
