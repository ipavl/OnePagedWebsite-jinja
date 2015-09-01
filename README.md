One-Paged Website
=================

A single-page website using [Flask](http://flask.pocoo.org), SQLite, and Jinja2.

For an AngularJS version, see [OnePagedWebsite-angular](https://github.com/ipavl/OnePagedWebsite-angular).

Set up
------

1. Run `app.py` to create the database
2. Edit the created `sqlite.db` file to add projects (note: `date` should be in the format `YYYY-MM-DD`, e.g. 2015-08-31, and `tags` should be a comma-separated list of strings)
3. Change the links and "About Me" instances in `templates/index.html` as appropriate
4. Change `site_title` and `site_tagline` in `app.py`

By default, there is only a "Project" model, but the app can easily be extended to support other models if desired.

Screenshot
----------

![](screenshot.png)