import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/inventory-management', methods=['POST'])
def evaluation():
    data = request.get_json()
    result = magicalBasket(data)
    return jsonify(result)


def magicalBasket(dict1):
    sum1 = 0
    for k, v in dict1.items():
        sum1 = sum1 + v
    return sum1 * 50