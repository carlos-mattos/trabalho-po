from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from solver import runSolver
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

class Test(Resource):
    @cross_origin()
    def post(self):
        limit_x1 = request.json['x1']
        limit_x2 = request.json['x2']
        result = runSolver(limit_x1, limit_x2)
        return result

api.add_resource(Test, '/test') 

if __name__ == '__main__':
   app.run(port=3001)