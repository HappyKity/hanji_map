from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/start')
def start():
    return render_template('input_city_name.html')


@app.route('/city_name')
def city_name():
    city = request.args['city']
    name = request.args['name']
    return render_template('print_city_name.html', city=city, name=name)


app.run(debug=True)
