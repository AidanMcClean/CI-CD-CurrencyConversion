from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)


def get_exchange_rate(base, target):
    pass


@app.route('/conversion', methods=['GET'])
def currency_converter():
    pass


@app.route('/status', methods=['GET'])
def status_checker():
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)