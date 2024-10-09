import os
import utils.config as config
from utils.scheduler import Scheduler
from flask import Flask
from dotenv import load_dotenv
from longport.openapi import Config
from route.admin import admin_route
from route.api import api_route
from apscheduler.schedulers.background import BackgroundScheduler

# 加载 .env 文件中的配置
load_dotenv('.env')
active_env = os.getenv('active')

# 加载环境文件
if active_env == 'develop':
    load_dotenv('develop.env', override=True)
elif active_env == 'product':
    load_dotenv('product.env', override=True)
else:
    raise ValueError(f"Unknown environment: {active_env}")

# 所有env变量
config.all_env = {key.lower(): value for key, value in os.environ.items()}

# 加载长桥的配置
config.long_bridge_config = Config(
    app_key = config.all_env.get("app_key"), 
    app_secret = config.all_env.get("app_secret"), 
    access_token = config.all_env.get("access_token")
)

# 创建一个Flask应用程序实例
app = Flask(__name__)

def process_database_data():
    scheduler = Scheduler(config.long_bridge_config)
    scheduler.run()

scheduler = BackgroundScheduler()
scheduler.add_job(func=process_database_data, trigger="interval", seconds=60)  # 定时任务60秒运行一次
scheduler.start()

# api路由注册
app.register_blueprint(api_route, url_prefix='/api')

# admin路由注册
app.register_blueprint(admin_route, url_prefix='/admin')

# 启动服务器
if __name__ == '__main__':
    app.run(debug=True,port=5001)
