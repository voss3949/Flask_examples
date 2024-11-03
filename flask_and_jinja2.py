from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
	def home():
    return render_template('index.html', name='World')

if __name__ == "__main__":
	app.run()
