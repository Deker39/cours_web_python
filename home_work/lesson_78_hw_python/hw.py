from flask import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ls = [request.form['input_one'], request.form['input_two'], request.form['input_three']]
        operation = request.form['radio']
        if operation == 'min':
            res = min(ls)
        elif operation == 'max':
            res = max(ls)
        else:
            res = sum(map(lambda x: int(x), ls)) / len(ls)

        print('data accepted')

        return redirect(url_for('success', number=res, operation=operation))

    context = {
        'title': 'Form',
        'content': 'example'
    }
    return render_template('main.html', context=context)


@app.route('/success')
def success():
    context = {
        'title': 'Result',
        'number': request.args.get('number'),
        'operation': request.args.get('operation')
    }
    return render_template('submit.html', context=context)


if __name__ == "__main__":
    app.run(debug=True)
