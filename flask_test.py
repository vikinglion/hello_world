#coding=utf-8

from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
   return "<h1>Hello Vikinglion!<h1>"

if __name__ == "__main__":
	app.run('0.0.0.0','8787')
