from flask import Flask
app = Flask(__name__)

@app.route('/')
def home_page():
    return 'Hello, World'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def say_name(name):
    return f'Hi, {name}!'

@app.route('/repeat/<int:num>/<string:str>')
def repeat(num,str):
    return f"{str}\n" * int(num)

"""
I found path from flask documentation about variables and route priority
This should capture any path, including longer non-defined paths like abc/xyc/2 that would be missed by a string var,
but is lower priority than the above more defined paths; therefore, it is the "catch everything else" path
"""
@app.route('/<path:path>') 
def catch_everything_else(path):
    return "Sorry! No response. Try again."

if __name__=="__main__":
    app.run(debug=True)