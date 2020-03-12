from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from src.controller.main.JsonFormat import PrCrisisResult
from src.controller.main.requestResult import prRequest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id



@app.route('/', methods=['POST', 'GET'])
def test():
    if request.method == 'POST':
        return redirect('/')

    else:
        return render_template('test.html')

@app.route('/output/', methods=['POST', 'GET'])
def output():
    print("test")
    if request.method == 'POST':
        task_content = request.form['content']
        prRequest()
        x,y = PrCrisisResult()
        f = open("templates/output.html", "w+")
        for i in x:
            f.write(i)
        for i in y:
            f.write(i)
        f.close()
        return redirect('/output/')

    else:
        return render_template('output.html')

if __name__ == "__main__":
    app.run(debug=True)
