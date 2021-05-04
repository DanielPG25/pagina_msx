from flask import Flask, render_template,request,abort
import json
import sys
import os
app = Flask(__name__)


with open('MSX.json') as f:
    juegosmsx=json.load(f)

@app.route('/',methods=["GET"])
def inicio():
	return render_template("inicio.html")

@app.route('/juegos',methods=["GET","POST"])
def juegos():
	if request.method=="GET":
		return render_template("juegos.html")
	else:
		cad = str(request.form.get("cad"))
		datos = []
		indicad = True
		for i in juegosmsx:
			if cad == "":
				dicc = {}
				dicc['id'] = i.get('id')
				dicc['nombre'] = i.get('nombre')
				dicc['desarrollador'] = i.get('desarrollador')
				datos.append(dicc)
				indicad = False
			elif str(i.get('nombre')).startswith(cad):
				dicc = {}
				dicc['id'] = i.get('id')
				dicc['nombre'] = i.get('nombre')
				dicc['desarrollador'] = i.get('desarrollador')
				datos.append(dicc)
				indicad = False
		if indicad:
			return render_template("juegos.html",cad=cad,error=True)
		else:	
			return render_template("listajuegos.html",datos=datos,cad=cad)
	

@app.route('/juego/<int:identificador>')
def detalle(identificador):
	datos = []
	ind = True
	for i in juegosmsx:
		if i.get('id') == identificador:
			dicc = {}
			ind = False
			dicc['nombre'] = i.get('nombre')
			dicc['desarrollador'] = i.get('desarrollador')
			dicc['sistema'] = i.get('sistema')
			dicc['distribuidor'] = i.get('distribuidor')
			dicc['categoria'] = i.get('categoria')
			dicc['año'] = i.get('año')
			datos.append(dicc)
	if ind:
		abort(404)
	return render_template("detallesjuegos.html",datos=datos)


port=os.environ["PORT"]
app.run('0.0.0.0',int(port), debug=True)