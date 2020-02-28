from flask import jsonify


def response(data, message, status):
    res = {
        "data": data,
        "message": message,
        "status": status
    }

    return jsonify(res)
