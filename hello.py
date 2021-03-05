from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'У меня получилось!!'


if __name__ == '__main__':
    print('Start working!!!')
    app.run(debug=True, host='0.0.0.0')
