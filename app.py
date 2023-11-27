from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.secret_key = 'Ol91xL&fP],dfsg1)L1X#K%dsgdfgdf'


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8095)
