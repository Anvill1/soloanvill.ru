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
            username = form.data['username'].rstrip()
            email = form.data['email']
            ip = request.remote_addr
            data = {
                'username': username,
                'email': email,
                'ip': ip
            }
            flash('Form successfully submitted!', "success") # Временно
            try:
                response = requests.post(backend_url, json=data)
                response.raise_for_status()
            except requests.exceptions.HTTPError as http_err:
                app.logger.error(f"HTTP error: {http_err}")
            except Exception as err:
                app.logger.error(f"Other error: {err}")

                raise ConnectionError('Couldn\'t connect to backend service')
            app.logger.info(f"Redeploy request by {username} created successfully")
            flash('Form successfully submitted!', "success")
            return redirect('/')
    return render_template("index.html", form=form)

@app.route('/metrics')
def metrics():
    return metrics.export()

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'),500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8095, debug=True)
