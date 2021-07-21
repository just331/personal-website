from flask import Flask, render_template

# Configure application
app = Flask(__name__)


@app.route('/index', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():
    title_text = 'Welcome To My Data Science & Logic Programming Portfolio Website [Under Construction!] '
    return render_template('/index.html',
                           title_text=title_text,
                           title="Data Science and Logic Programming",
                           id="index")


# About Me page
@app.route('/about', methods=['POST', 'GET'])
def about():
    title_text = 'Recent Texas Tech University graduate with a Master\'s degree in Computer Science. Interests in ' \
                 'Data Science and Logic Programming. Below is a brief timeline of my career so far. '
    return render_template('/about.html',
                           title_text=title_text,
                           title="About Me",
                           id="about")


@app.route('/portfolio', methods=['POST', 'GET'])
def portfolio():
    title_text = 'Here are a few of my favorite projects that I have completed throughout my educational career.'
    return render_template('/portfolio.html',
                           title_text=title_text,
                           title="Portfolio",
                           id="portfolio")
