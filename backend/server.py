from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from solver import runSolver

app = Flask(__name__)
api = Api(app)


class Test(Resource):
    def get(self):
        result = runSolver()
        return jsonify(result)


api.add_resource(Test, '/test') 

if __name__ == '__main__':
    app.run()