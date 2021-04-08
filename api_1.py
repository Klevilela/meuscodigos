from flask import Flask, jsonify
import json

app = Flask(__name__)

with open('quotes.json', 'r')as arquivo:
    abrir = arquivo.read()

obj = json.loads(abrir)

@app.route('/')
def inicio():
    return 'Olá'

@app.route('/quotes')
def quotes():
    #abrir = open('quotes.json')
    #carrega = json.load(abrir)
    return jsonify(obj)

'''@app.route('/quotes/<x>')
def indice(x):
    abrir = open('quotes.json', 'r')
    carrega = json.load(abrir)
    l = [carrega]
    for i in l:
        return jsonify(i[int(x)])

@app.route('/quotes/length')
def tamanho():
    abrir = open('quotes.json', 'r')
    carrega = json.load(abrir)
    for i, e in enumerate(abrir):
        i += 1
    return str(i)
'''
if __name__ == '__main__':
    app.run(debug=True)