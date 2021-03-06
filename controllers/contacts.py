from models import Contact
from helpers import helper
from flask import request


def create():
    data = request.json

    insert_id, message, status = Contact.create(data)

    if status != 200:
        return helper.response({"title": message}, "fail", status)
    else:
        return helper.response({"id": insert_id}, "success", status)


def update(id):
    data = request.json

    updated_id, message, status = Contact.update(id, data)

    if status != 200:
        return helper.response({"title": message}, "fail", status)
    else:
        return helper.response({"id": updated_id}, "success", status)


def delete(id):
    deleted_id, message, status = Contact.delete(id)

    if status != 200:
        return helper.response({"title": message}, "fail", status)
    else:
        return helper.response({"id": deleted_id}, "success", status)


def lists():
    records, status = Contact.list()

    if status != 200:
        return helper.response({}, records, status)
    else:
        results = []
        for record in records:
            data = {
                "id": record[0],
                "firstName": record[1],
                "lastName": record[2],
                "email": record[8]
            }
            results.append(data)

        return helper.response(results, "success", status)


def details(id):
    records, status = Contact.detail(id)

    if status != 200:
        return helper.response({}, records, status)
    else:
        results = []
        for record in records:
            data = {
                "id": record[0],
                "firstName": record[1],
                "lastName": record[2],
                "address": record[3],
                "city": record[4],
                "state": record[5],
                "zipCode": record[6],
                "phone": record[7],
                "email": record[8]
            }
            results.append(data)

        return helper.response(results, "message", "success")
