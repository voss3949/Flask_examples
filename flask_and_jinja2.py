from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('C:\Users\12245\OneDrive\Documents\Python_Projects\index.html', name='World')

if __name__ == "__main__":
	app.run()
