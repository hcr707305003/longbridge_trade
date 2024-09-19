import os
from flask import Flask
from dotenv import load_dotenv
from longport.openapi import QuoteContext, Config

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
all_env = {key.lower(): value for key, value in os.environ.items()}

# 初始化配置
login_bridge_config = Config(app_key = all_env.get("app_key"), app_secret = all_env.get("app_secret"), access_token = all_env.get("access_token"))

# 创建一个Flask应用程序实例
app = Flask(__name__)

# 定义一个路由
@app.route('/')
def home():
    ctx = QuoteContext(login_bridge_config)
    resp = ctx.brokers("700.HK")
    print(resp)
    return "Hello, Flask!"

@app.route('/subscribe')
def subscribe():
    from subscribe_quote import Quote 
    Quote(
        login_bridge_config
    ).subscribe()
    return 'true'

# 启动服务器
if __name__ == '__main__':
    app.run(debug=True,port=5001)
