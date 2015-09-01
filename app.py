from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Text, Date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
db = SQLAlchemy(app)


class Project(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(Text, unique=False)
    date = Column(Date, unique=False)
    description = Column(Text, unique=False)

db.create_all()


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
