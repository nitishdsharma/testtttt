from flask import Flask, jsonify, request

# Flask app
app = Flask(__name__)

# ‘/’ URL is bound with welcome() function
@app.route('/', methods = ['GET'])
def welcome():
    data = "Welcome User"
    return data

# ‘/reverse/<teststring>’ URL is bound with string reverse function
@app.route('/reverse/<string:teststring>', methods = ['GET'])
def reverse(teststring):
    return jsonify({'Reversed string is': teststring[::-1]})

# Error handling function
@app.errorhandler(404) 
def invalid_route(err): 
    return ("Either user is hitting an unavailable endpoint or teststring is not passed. \nPlease provide a valid endpoint and string to reverse, example: reverse/teststring")

# Driver function
if __name__ == '__main__':
	app.run(debug = True, port=5002, host="0.0.0.0")