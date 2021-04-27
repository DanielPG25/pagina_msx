from flask import Flask, render_template,request,abort
import json
import sys
import os
app = Flask(__name__)


with open('./MSX.json') as f:
    juegosmsx=json.load(f)

@app.route('/',methods=["GET"])
def inicio():
	return render_template("inicio.html")

@app.route('/juegos',methods=["GET"])
def juegos():
	return render_template("juegos.html")

@app.route('/listajuegos',methods=["POST"])
def listajuegos():
	cad = request.form.get("juego")
	datos = []
	for i in juegosmsx:
		if i.get("nombre").startswith(cad):
			dicc = {}
			dicc['id'] = i.get('id')
			dicc['nombre'] = i.get('nombre')
			dicc['desarrollador'] = i.get('desarrollador')
			datos.append(dicc)
	return render_template("listajuegos.html",datos=datos,cad=cad)


app.run(debug=True)