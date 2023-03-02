from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__, template_folder='templates')

class Person:
    def __init__(self, name, sname, addr, phone, comm, img):
        self.img = img
        self.comm = comm
        self.name = name
        self.sname = sname
        self.addr = addr
        self.phone = phone



@app.route("/")
def index():
    persons = [
        Person('Alex', 'Smith', 'Krasnova 4', '339994', 'kek', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScgsJTy2dl-Tr4m1amid5OZyNTg-c2KlgbmnjO947w&s'),
        Person('Den', 'Smith', 'Krasnova 4', '339994', 'kek', 'https://images.unsplash.com/photo-1575936123452-b67c3203c357?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8aW1hZ2V8ZW58MHx8MHx8&w=1000&q=80'),
        Person('VAr', 'Smith', 'Krasnova 4', '339994', 'kek', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQPCXISA7AWonO3J24GKCgtJ9e4OTuaJHSBM7rcN3j28GfR6eJAJTe1Gi_AlJpG6wuFnCs&usqp=CAU'),
        Person('MAria', 'Smith', 'Krasnova 4', '339994', 'kek', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTL8cTUcRmxOcXuGl91pj65WaF5dx_WoLqpYWUt5LuZZ7gO4KVN4ImyOD_loWR-WNQjkwU&usqp=CAU'),

    ]
    return render_template('index.html', persons=persons)
    #                        **{'name': 'Alex',
    #                         'age': 12,
    #                         'phone': '+380986074515',
    #                         'addr': 'link223'}
    #                        )


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
