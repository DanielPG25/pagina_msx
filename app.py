from flask import Flask, render_template,request,abort
app = Flask(__name__)

@app.route('/',methods=["GET"])
def inicio():
	return render_template("inicio.html")



app.run(debug=True)