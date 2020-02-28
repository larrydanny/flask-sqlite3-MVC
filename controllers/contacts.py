from models import Contact
from helpers import helper


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
