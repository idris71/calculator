from flask import Flask,request,jsonify


app = Flask(__name__)

#http://127.0.0.1:5000/api.calculator.com/add?num1=4&num2=89
@app.route("/api.calculator.com/add",methods=['GET'])
def api_add():
    num1 = int(request.args["num1"])
    num2 = int(request.args["num2"])
    return jsonify({"operation":"addition","Result":num1+num2})


#http://127.0.0.1:5000/api.calculator.com/sub?num1=4&num2=89
@app.route("/api.calculator.com/sub",methods=['GET'])
def api_sub():
    num1 = int(request.args["num1"])
    num2 = int(request.args["num2"])
    return jsonify({"operation":"subtraction","Result":num1-num2})

@app.route("/api.calculator.com/multiply",methods=['GET'])
def api_mul():
    num1 = int(request.args["num1"])
    num2 = int(request.args["num2"])
    return jsonify({"operation":"multiplication","Result":num1*num2})

@app.route("/api.calculator.com/divide",methods=['GET'])
def api_div():
    num1 = float(request.args["num1"])
    num2 = float(request.args["num2"])
    return jsonify({"operation":"division","Result":num1/num2})


if(__name__=="__main__"):
    app.run(debug=True)
