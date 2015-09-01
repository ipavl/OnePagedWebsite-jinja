from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.templating import render_template
from sqlalchemy import Column, Integer, Text, Date

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
db = SQLAlchemy(app)

# Site configuration
site_title = 'Your Name'


class Project(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(Text, unique=False)
    date = Column(Date, unique=False)
    description = Column(Text, unique=False)

db.create_all()


@app.route('/')
def index():
    return render_template('index.html', site_title=site_title)


if __name__ == '__main__':
    app.run()
