from flask import Flask, render_template, flash

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/my-work")
def work():
    return render_template("work.html")


if __name__ == "__main__":
    app.run(debug=True)