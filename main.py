import os
from flask import Flask, render_template
import yfinance as yf

template_dir = os.path.abspath('C:/Users/12245/OneDrive/Documents/Python_Projects/MyDashboard/')

app = Flask(__name__, template_folder=template_dir)

name = 'Joshua'
btc_price = yf.Ticker("BTC-USD").history(period='1d')['Close'].iloc[-1]

@app.route("/")
def homepage():
    return render_template("index.html", name=name, btc_price=btc_price)


if __name__ == "__main__":
    app.run(port=5000)
