from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL

app = Flask(__name__)
Bootstrap(app)

#DB configuration
app.config('MYSQL_HOST')
app.config('MYSQL_USER')

@app.route('/')
def index():
    colors = ['Red', 'Blue', 'Green']
    return render_template('index.html', colors=colors)
    #return redirect(url_for('about')) -- перенаправление

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/css')
def css():
    return render_template('css.html')

if __name__ == '__main__':
    app.run(debug=True,port=5001)

 print('hello, world!')
