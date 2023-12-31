from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def showdashboard():
    return render_template('index.html')


@app.route('/dashboard.html')
def dashboard():
    return render_template('dashboard.html')

if __name__== '__main__':
    app.run(debug=True)
    