from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from solver import runSolver
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

def formatCsvReceived():
    # read csv file from temp.csv
    with open('temp.csv', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        lines = [line for line in lines if line != ['']]
    
    variables = lines[0].split(',')
    variables = [var for var in variables if var != '']
    lines = lines[2:]
    for i in range(len(lines)):
        lines[i] = lines[i].split(',')
        lines[i] = [var for var in lines[i] if var != '']
        del lines[i][0]
    return variables, lines

class Test(Resource):
    @cross_origin()
    def post(self):
        file = request.files['file']
        file.save(os.path.join(os.getcwd(), 'temp.csv'))
        variables, lines =  formatCsvReceived()
        result = runSolver(variables, lines)
        return ""

api.add_resource(Test, '/test') 

if __name__ == '__main__':
   app.run(port=3001, debug=True)