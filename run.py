from flask import Flask
from flask_restx import Api

from api.tasks.routes import ns as tasks_ns
from api.uprocs.routes import ns as uprocs_ns



app = Flask(__name__)
api = Api(app)
api.add_namespace(tasks_ns)
api.add_namespace(uprocs_ns)


if __name__ == '__main__':
    app.run(port=5132)
