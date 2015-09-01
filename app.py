from datetime import datetime
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.templating import render_template
from markdown import markdown
from sqlalchemy import Column, Integer, Text

app = Flask(__name__, static_url_path='')
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
db = SQLAlchemy(app)

# Site configuration
site_title = 'Your Name'
site_tagline = 'Your Title or Tagline'


class Project(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(Text, unique=False)
    date = Column(Text, unique=False)
    tags = Column(Text, unique=True)
    description = Column(Text, unique=False)

db.create_all()


@app.route('/')
def index():
    projects = Project.query.order_by(Project.date.desc()).all()
    print(projects)
    return render_template('index.html',
                           site_title=site_title,
                           site_tagline=site_tagline,
                           projects=projects)


@app.template_filter('md2html')
def markdown_to_html(s):
    """
    Renders a Markdown-formatted string as HTML.
    """
    return markdown(s)


@app.template_filter('projectdate')
def filter_project_date(s):
    """
    Converts a string to the format "Month Year" (e.g. January 2015).
    """
    return datetime.strptime(s, '%Y-%m-%d').strftime('%B %Y')


@app.template_filter('splitcomma')
def split_by_comma(s):
    """
    Splits a comma-delimited string.
    """
    return s.strip().split(",")

if __name__ == '__main__':
    app.run()
