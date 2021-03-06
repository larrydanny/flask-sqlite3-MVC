import flask
from controllers import health
from controllers import contacts

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def health():
    return health.hello()


@app.route('/contacts', methods=['POST'])
def create():
    return contacts.create()


@app.route('/contacts/<id>', methods=['PUT'])
def update(id):
    return contacts.update(id)


@app.route('/contacts/<id>', methods=['DELETE'])
def delete(id):
    return contacts.delete(id)


@app.route('/contacts', methods=['GET'])
def get_list():
    return contacts.lists()


@app.route('/contacts/<id>', methods=['GET'])
def get_details(id):
    return contacts.details(id)


app.run()
