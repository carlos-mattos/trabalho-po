from flask import Flask, request, send_file, jsonify
from flask_restful import Api
from solver import runSolver
from flask_cors import CORS, cross_origin
import os
from fpdf import FPDF

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

def createPdf(result):
    # if already exists, delete it
    if os.path.exists('result.pdf'):
        os.remove('result.pdf')

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 15)
    pdf.cell(200, 10, txt = "Resultados", ln = 2, align = 'C')
    pdf.set_font("Arial", size = 13)
    pdf.cell(200, 10, txt = "semente 1: " + str(result["semente1"]), ln = 2, align = 'L')
    pdf.cell(200, 10, txt = "semente 2: " + str(result["semente2"]), ln = 2, align = 'L')
    pdf.cell(200, 10, txt = "semente 3: " + str(result["semente3"]), ln = 2, align = 'L')
    pdf.cell(200, 10, txt = "semente 4: " + str(result["semente4"]), ln = 2, align = 'L')
    pdf.cell(200, 10, txt = "semente 5: " + str(result["semente5"]), ln = 2, align = 'L')
    pdf.cell(200, 10, txt = "maquina: " + str(result["maquina"]), ln = 2, align = 'L')
    pdf.cell(200, 10, txt = "pessoa: " + str(result["pessoa"]), ln = 2, align = 'L')
    pdf.output("results.pdf")  

def formatCsvReceived():
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
    return variables, lines


@cross_origin()
@app.route('/solve', methods=['POST'])
def solve():
    file = request.files['file']
    file.save(os.path.join(os.getcwd(), 'temp.csv'))
    variables, lines =  formatCsvReceived()
    result = runSolver(variables, lines)
    createPdf(result)  
    return jsonify(ok=True)

@cross_origin()
@app.route('/download-results', methods=['POST'])
def teste():
    return send_file('results.pdf', mimetype='application/pdf')
    

if __name__ == '__main__':
   app.run(port=3001, debug=True)