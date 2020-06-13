# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]
from flask import Flask, render_template, send_file
from flask_cors import CORS
from utility import load_blueprints
from jinja2.exceptions import TemplateNotFound
import logging
import sys
import os 
import config

def create_flask_app():
	app = Flask(__name__, template_folder="build")
	app.secret_key = config.secret_key
	CORS(app)
	blueprints = load_blueprints()
	for bp in blueprints: app.register_blueprint(bp)
	return app

app = create_flask_app()

@app.route('/')
def index():
    try:
	    return render_template('index.html')
    except TemplateNotFound as e:
        return "No Frontend found. Make sure to build the reactjs frontend, and copy that build folder to server root"

@app.route('/static/css/<filename>')
def css(filename):
	return send_file(os.path.join(os.getcwd(), "build/static/css/%s" % filename))

@app.route('/static/js/<filename>')
def js(filename):
	return send_file(os.path.join(os.getcwd(), "build/static/js/%s" % filename))

@app.route('/static/media/<filename>')
def media(filename):
	return send_file(os.path.join(os.getcwd(), "build/static/media/%s" % filename))
		

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(port=8080, debug=True)

# [END gae_python37_app]
