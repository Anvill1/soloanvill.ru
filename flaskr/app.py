import requests, logging
from flask import Flask, render_template, request, redirect, flash
from forms import *
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
app.secret_key = 'Ol91xL&fP],dfsg1)L1X#K%dsgdfgdf'

logging.basicConfig(level=logging.INFO)

backend_url = 'http://soloanvill-backend/api/deployment/create'

metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Application info', version='1.0.3')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = RedeployForm()

    if request.method == "POST":
        if form.validate_on_submit():
            flash('Form sucessfully submitted!', "success")
            username = form.data.rstrip()
            email = form.data
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
                app.logger.error(f"HTTP error: {http_err}")
            except Exception as err:
                app.logger.error(f"Other error: {err}")
            return redirect('/')
    return render_template("index.html", form=form)

@app.route('/metrics')
def metrics():
    return metrics.export()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8095, debug=True)
