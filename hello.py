from cloudant import Cloudant
from flask import Flask, request, render_template, jsonify, redirect, url_for, send_from_directory
from flask_bootstrap import Bootstrap
import atexit
import os
import json

# import PIL
# from PIL import Image
# import simplejson
# import traceback

# from werkzeug import secure_filename

from lib.upload_file import uploadfile
from lib.handleDataset import SetCodenation, HandlerDataset

#####################################################################################################

app = Flask(__name__)

app.config['SECRET_KEY'] = 'hard to guess string'
app.config['UPLOAD_FOLDER'] = 'data/'
app.config['THUMBNAIL_FOLDER'] = 'data/thumbnail/'
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['txt', 'jpg', 'jpeg',
                        'doc', 'docx', 'csv', 'xsxl'])
IGNORED_FILES = set(['.gitignore'])

bootstrap = Bootstrap(app)

db_name = 'mydb'
client = None
db = None

if 'VCAP_SERVICES' in os.environ:
    vcap = json.loads(os.getenv('VCAP_SERVICES'))
    print('Found VCAP_SERVICES')
    if 'cloudantNoSQLDB' in vcap:
        creds = vcap['cloudantNoSQLDB'][0]['credentials']
        user = creds['username']
        password = creds['password']
        url = 'https://' + creds['host']
        client = Cloudant(user, password, url=url, connect=True)
        db = client.create_database(db_name, throw_on_exists=False)
elif "CLOUDANT_URL" in os.environ:
    client = Cloudant(os.environ['CLOUDANT_USERNAME'], os.environ['CLOUDANT_PASSWORD'], url=os.environ['CLOUDANT_URL'], connect=True)
    db = client.create_database(db_name, throw_on_exists=False)
elif os.path.isfile('vcap-local.json'):
    with open('vcap-local.json') as f:
        vcap = json.load(f)
        print('Found local VCAP_SERVICES')
        creds = vcap['services']['cloudantNoSQLDB'][0]['credentials']
        user = creds['username']
        password = creds['password']
        url = 'https://' + creds['host']
        client = Cloudant(user, password, url=url, connect=True)
        db = client.create_database(db_name, throw_on_exists=False)

# On IBM Cloud Cloud Foundry, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
port = int(os.getenv('PORT', 8000))

@app.route("/clientone", methods=['GET'])
def client_one():
    level_array = ["A", "B", "C"]
    result = {}
    setCodenationInstance = SetCodenation()

    for level in level_array:
        setCodenation = setCodenationInstance.selectSet(full=False, number="one", level=level)
        data = HandlerDataset(setCodenation).client_obj_array
        key = f"message_{level}"
        result[key] = data

    return render_template('dataset_actual/portifolio_demo.html', **result)

@app.route("/clienttwo", methods=['GET'])
def client_two():
    level_array = ["A", "B", "C"]
    result = {}

    setCodenationInstance = SetCodenation()

    for level in level_array:
        setCodenation = setCodenationInstance.selectSet(full=False, number="two", level=level)
        data = HandlerDataset(setCodenation).client_obj_array
        key = f"message_{level}"
        result[key] = data

    return render_template('dataset_actual/portifolio_demo.html', **result)

@app.route("/clientthree", methods=['GET'])
def client_three():
    level_array = ["A", "B", "C"]
    result = {}

    setCodenationInstance = SetCodenation()

    for level in level_array:
        setCodenation = setCodenationInstance.selectSet(full=False, number="three", level=level)
        data = HandlerDataset(setCodenation).client_obj_array
        key = f"message_{level}"
        result[key] = data

    return render_template('dataset_actual/portifolio_demo.html', **result)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@atexit.register
def shutdown():
    if client:
        client.disconnect()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
