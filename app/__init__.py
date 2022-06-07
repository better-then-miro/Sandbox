from flask import Flask
from flask_socketio import SocketIO

# создаем наше приложение как инстанс фласка
app = Flask(__name__, static_folder='dist/',  static_url_path='/')

#в действительности нам нужна надстройка над фласком в виде сокетио. Обратите 
#внимание, что именно этот socketio мы импортируем в sandbox.py
socketio = SocketIO(app, cors_allowed_origins='*')

# такой забавный импорт в самом конце нужен, чтобы избежать циклических инклудов
# про которые когда-то давно рассказывал гатилов. Если глянете в routes.py, то
# увидите, что там мы инклудим наш socketio и app(именно инстансы объектов)
from app import routes