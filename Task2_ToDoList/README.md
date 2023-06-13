# GitHub Codespaces ♥️ Flask

Welcome to your shiny new Codespace running Flask! We've got everything fired up and running for you to explore Flask.

You've got a blank canvas to work on from a git perspective as well. There's a single initial commit with the what you're seeing right now - where you go from here is up to you!

Everything you do here is contained within this one codespace.
To run this application:

```
flask --debug run
```
----

1. Templates: This folder stores the templates like index.html files.

2. Static: This folder stores static files that are rendered same to same as the file. eg- details.txt.

3. Flask-SQLAlchemy package:
```
pip install flask-sqlalchemy
```
SQLAlchemy is an ORM(Object-relational mapping) mapper. It provides facilities to have changes in the database using Python.

4. Jinja2 snippet toolkit extension install
```
Jinja2 is a modern day templating language for Python developers. It is used to create HTML, XML or other markup formats that are returned to the user via an HTTP request.
```
- Jinja2 is a templating engine, it is useful when you build flask apps(jab koi python variable send krte hn tub)

- used to create rows of todo table:
database(sqlite) se query kar k sara data ek variable me store karne k baad, html table me rows-columns format me display kar rhe hn.

5. jfor: jinja2 for loop (python's)

```diff
+ <th scope="row">{{loop.index}}</th> ye karna sahi rahega (index k hisaab se serial no show krega)
- <th scope="row">{{todo.sno}}</th> db se row delete hone par next number se show krega
```

6. @app.route("/", methods = ['GET', 'POST']) 

    catch - catch khelna hai to dena parega

7. if you need request method or redirect to a page, you must first import them

8. Yes it is legal:
```
<a href="/delete/{{todo.sno}}" type="button" class="btn btn-outline-danger btn-sm">Delete</button>
```

9. Template Inheritance:
eg- There is a navigation bar in all 10 pages of the website. If you want to change "About" to "About Us", you'll have to edit in all 10 pages. 
But by using Template Inheritance, you can do it from a single place.
header, footer, navigation bar, etc can be done by this technique (here, <b>base.html</b>).

10. base.html
This file contains everything that is common in all pages like header, footer, navigation bar, etc.

11. gunicorn
You can use it to serve your app in multiple threads.
```
pip install gunicorn
```

then

```
pip freeze > requirements.txt (it's good practice)
```
# Let's deploy the app into Heroku

12. Create Procfile 
This file is used by Heroku to deploy the application