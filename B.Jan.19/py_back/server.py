# 사용자의 요청에 응답하는 서버 개발 : 백엔드 + 화면
# 프레임워크 - 필요한 기능들을 붚품화해서 조립하는 방식
# templates - html. static - css, js

from flask import Flask, request, render_template

app = Flask(__name__)


# 기능
# 배포서줄자(deployment descriptor : 함수와 주소의쌍 -여기서는 aaa와 /hello)
@app.route('/hello')
def aaa():
    # 플라스크 함수의 리턴은 반드시 문자열
    return render_template("input_name.html")


@app.route('/name1', methods=['get'])
def input_name():
    username = request.args["username1"]
    return render_template('index.html', username=username)


@app.route('/name2', methods=['post'])
def print_name():
    # get방식 요청 데이터 : request.args
    # post방식 요청 데이터 : request.form
    username = request.form["username2"]
    age = request.form["age"]
    return render_template('index.html', printname=username, printage=age)


print(app.url_map)

# 실행되는 url : 127.0.0.1:5000
# debug란 개발 모드
app.run(debug=True)
