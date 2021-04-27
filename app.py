from flask import Flask, render_template,request,abort
app = Flask(__name__)

@app.route('/',methods=["GET"])
def inicio():
	return render_template("inicio.html")

@app.route('/juegos',methods=["GET"])
def juegos():
	return render_template("juegos.html")


app.run(debug=True)