from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'É o FRAMENGO !!'

@app.route('/clients')
def getclients():
    return 'Jose, João, Tiringa'
if __name__ == '__main__':
    app.run(debug=True)
