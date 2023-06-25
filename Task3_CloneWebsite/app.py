from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    '''This is the Homepage'''
    return render_template("index.html")

@app.route('/academics', methods=['GET', 'POST'])
def academics():
    return render_template("academics.html")

@app.route('/activities', methods=['GET', 'POST'])
def activities():
    return render_template("activities.html")

@app.route('/faculty', methods=['GET', 'POST'])
def faculty():
    return render_template("faculty.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")

@app.route('/message', methods=['GET', 'POST'])
def message():
    return render_template("message.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template("contact.html")

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
