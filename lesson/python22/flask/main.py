from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__, template_folder='templates')


@app.route("/")
def index():
    return render_template('index.html',
                           **{'name': 'Alex',
                            'age': 24,
                            'phone': '+380986074515'}
                           )


@app.route("/hello")
def hello():
    return 'Hello World'


# 1. string, make_response()
@app.route("/user/<id>/")
def user(id: int):
    return f"<h1>user #{id} page</h1>"


@app.route("/profile")
def profile():
    res = make_response("Profile page")
    res.headers['Content-Type'] = 'text/plain'
    res.headers['MyHeader'] = 'texttexttext'
    return ("Profile page", 200,
            {'Content-Type': 'text/plain', 'MyHeader': 'texttexttext'})


@app.route("/users")
def users():
    return redirect("http://127.0.0.1:5000/user/40/")


@app.errorhandler(404)
def error_not_found(error):
    return "NOT FOUND YES\n" + str(error)


# app.add_url_rule('/','index', index)


if __name__ == '__main__':
    app.run(debug=True)
