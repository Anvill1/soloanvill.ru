from flask import Flask, render_template, request, redirect
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
app.secret_key = 'Ol91xL&fP],dfsg1)L1X#K%dsgdfgdf'

metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Application info', version='1.0.3')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/metrics')
def metrics():
    return metrics.export()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8095)
