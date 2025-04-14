from flask import Flask
from app.routes.api import api_bp
from app.utils.data_loader import load_testnet_data  # 👈 Добавим эту строку

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_bp)

    # 🔁 Загружаем данные при запуске
    with app.app_context():
        load_testnet_data()

    return app
