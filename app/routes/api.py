from flask import Blueprint, jsonify
from app.utils.data_loader import load_testnet_data
from app.utils.filters import filter_testnets

api = Blueprint('api', __name__)

@api.route("/api/testnets", methods=["GET"])
def get_testnets():
    data = load_testnet_data()
    filtered_data = filter_testnets(data)
    return jsonify(filtered_data)


@api.route("/", methods=["GET"])
def home():
    return "🚀 API работает! Добавь /api/testnets для получения тестнетов."

@api.route("/api/testnets/filtered", methods=["GET"])
def get_filtered_testnets():
    all_data = collect_all_testnet_data()
    filtered_data = filter_testnets(all_data)
    return jsonify(filtered_data)


# Эта строка обязательна — мы её импортируем в app/__init__.py
api_bp = api
