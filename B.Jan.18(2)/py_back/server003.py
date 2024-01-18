from flask import Flask, request, render_template
import datetime


app = Flask(__name__)

# 태어난 년도를 입력받아 나이를 출력


# 년도를 입력하는 화면
@app.route("/input_year")
def input_year():
    return render_template("sample4.html")


# 결과를 출력하는 화면
@app.route("/result_age")
def result_age():
    this_year = datetime.datetime.now().year
    result_year = int(request.args['year'])
    age = this_year - result_year
    return render_template("sample4_view.html", age=age)


app.run()
