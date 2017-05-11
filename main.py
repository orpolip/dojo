from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def display():
    return render_template("request.html")


@app.route('/request-counter', methods=["POST"])
def count_get():
    pass


if __name__ == '__main__':
    app.run(debug=True)
