from flask import Flask, render_template

# Configure application
app = Flask(__name__)


@app.route('/index', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():
    greeting = 'Welcome to My A.I. / Data Science Portfolio Website'

    return render_template('/index.html',
                           greeting=greeting)


@app.route('/about', methods=['POST', 'GET'])
def about():
    title_text = 'About'
    return render_template('/about.html',
                           title_text=title_text)
