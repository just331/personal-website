from flask import Flask, render_template

# Configure application
app = Flask(__name__)


@app.route('/index', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():
    greeting = 'Welcome to My A.I. / Data Science Portfolio Website [Under Construction!]'

    return render_template('/index.html',
                           greeting=greeting)


# About Me page
@app.route('/about', methods=['POST', 'GET'])
def about():
    about_me = 'About me'
    return render_template('/about.html',
                           about=about_me)


@app.route('/portfolio', methods=['POST', 'GET'])
def portfolio():
    port = 'Portfolio Page'
    return render_template('/portfolio.html',
                           port=port)
