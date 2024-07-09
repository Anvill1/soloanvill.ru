import requests, logging
from flask import Flask, render_template, request, redirect
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
app.secret_key = 'Ol91xL&fP],dfsg1)L1X#K%dsgdfgdf'

logging.basicConfig(level=logging.INFO)

backend_url = 'http://soloanvill-backend/api/deployment/create'

metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Application info', version='1.0.3')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        username = request.form['username'].rstrip()
        email = request.form['email']
        ip = request.remote_addr
        data = {
            'username': username,
            'email': email,
            'ip': ip
        }
        try:
            response = requests.post(backend_url, json=data)
            response.raise_for_status()
            app.logger.info(f"Redeploy request by {username} created successfully")
        except requests.exceptions.HTTPError as http_err:
            app.logger.error(f"HTTP ошибка: {http_err}")
        except Exception as err:
            app.logger.error(f"Другая ошибка: {err}")
        return redirect('/')
    else:
        return render_template("index.html")

@app.route('/metrics')
def metrics():
    return metrics.export()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8095)
