# coding: utf-8
from leancloud import Engine, LeanEngineError

from cloud_func.cloud_env import APP_ID, MASTER_KEY
from cloud_func.sign import engine as sign_engine

engine = Engine()

# 分离云函数, 从别的地方导入, 并汇总注册
engine.register(sign_engine)
