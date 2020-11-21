from flask import Flask

app = Flask(__name__)


@app.route('/welcome')
def welcome():
    "Return welcome html"

    html = "<html><body><h1>Welcome!</h1></body></html>"
    return html