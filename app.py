import pandas as pd
from flask import Flask, jsonify, request, send_file
import mainModel

# app
app = Flask(__name__)

# routes
@app.route('/', methods=['POST'])

def predict():
    # get data
    data = request.get_json(force=True)

    if data == "percentageOfMoneyGraph":
        filename = mainModel.percentageOfMoneyGraph(data)
    elif data == "amountSpentDaily":
        filename = mainModel.amountSpentDaily(data)
    elif data == "dailyExpenses":
        filename = mainModel.dailyExpenses(data)
    elif data == "predictExpenses":
        filename = mainModel.predictExpenses(data)
    else:
        filename="none"
            # send back to browser
    output = {'results': filename}

    # return data
    return jsonify(results=output)

#    return send_file(filename, mimetype='image/jpeg')

    
    

if __name__ == '__main__':
    app.run(port = 5000, debug=True)