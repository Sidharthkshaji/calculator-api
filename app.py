from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "This is a simple calculator"

@app.route('/add')
def add():
    a = float(request.args.get('a',0))
    b = float(request.args.get('b',0))
    return jsonify({
        "First Number " : a,
        "Second Number " : b,
        "Sum" : a+b
    })
@app.route('/sub')
def sub():
    a = float(request.args.get('a',0))
    b = float(request.args.get('b',0))
    return jsonify({
        "First Number " : a,
        "Second Number " : b,
        "Difference" : a-b
    })
@app.route('/mul')
def mul():
    a = float(request.args.get('a',0))
    b = float(request.args.get('b',0))
    return jsonify({
        "First number" : a,
        "Second number" : b,
        "product" : a*b
    })
@app.route('/div')
def div():
    a = float(request.args.get('a',0))
    b = float(request.args.get('b',0))
    if b==0 : return "Cannot divided by 0"
    return jsonify({
        "First number" : a,
        "Second number" : b,
        "quotient" : a/b
    })
@app.route('/exp')
def exp():
    a = float(request.args.get('a',0))
    b = float(request.args.get('b',0))
    return jsonify({
        "First Number " : a,
        "Second Number " : b,
        "Exponentiation" : a**b
    })
@app.route('/rem')
def rem():
    a = float(request.args.get('a',0))
    b = float(request.args.get('b',0))
    if b==0 : return "Cannot divided by 0"
    return jsonify({
        "First Number " : a,
        "Second Number " : b,
        "Reminder" : a%b
    })

if __name__ == '__main__':
    app.run(debug=True)