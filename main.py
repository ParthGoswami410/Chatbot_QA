from flask import Flask, render_template, request, jsonify
from app.api import api_blueprint

app = Flask(__name__)
app.register_blueprint(api_blueprint)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
