#https://flask-web-academy.com/article/flask-debug/

#Flaskクラスをインポート
from flask import Flask,render_template,url_for
import logging
#from setting_logger import set_logger, getLogger
#from flask_debugtoolbar import DebugToolbarExtension


#Flaskのインスタンス化
app= Flask(__name__)
app.debug = True

#ログ設定
#set_logger()
#logger = getLogger(__name__)
#logging.basicConfig(filename='debug.log', encoding='utf-8', level=logging.DEBUG)
'''
#ログを書き込むとき
logger.debug("デバッグ用ログ")
logger.info("普通のログ")
logger.warning("やば目のログ")
'''

#以下、DebugToolbarの設定(Flask 3では使えない？？)
'''
#SECRET_KEYを設定する
app.config["SECRET_KEY"]="abcdefg"
#ログレベルを設定する
app.logger.setLevel(logging.DEBUG)
#リダイレクトを中断しないようにする
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"]= False
#DebugToolbarExtensionにアプリケーションをセットする
#toolbar = DebugToolbarExtension(app)  #・・・使えない。。
'''


#URLと実行する関数をマッピング
@app.route("/")
def index():
    return "Hello, Flaskbook!"


@app.route("/hello/<name>",
           methods=["GET","POST"],
           endpoint="hello-endpoint")
def hello(name):
    return f"Hello, {name}!"

@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html",name=name)

with app.test_request_context():
    print(url_for("index"))
    print(url_for("hello-endpoint",name="world"))
    print(url_for("show_name",name="ichiro",page="1"))
