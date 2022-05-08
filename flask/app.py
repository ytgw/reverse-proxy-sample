from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    html = '<h1>Hello Flask!</h1>\n'
    for key, val in request.headers.items():
        html += f'<p>{key}: {val}</p>\n'
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
