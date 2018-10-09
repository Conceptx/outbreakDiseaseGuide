from flask import Flask, jsonify, request, Response, url_for, render_template, redirect
from flask_cors import CORS
from models import client, errors
import json
import gunicorn

app = Flask(__name__)
CORS(app)

try:
    # database configuration
    db = client['kudziya']

    @app.route('/cholera')
    def cholera():

        # get indexed diseases
        diseases = []
        information = []

        query = db.Diseases.find({}, {'Name':'1'})
        for i in query:
            diseases.append(i['Name'])

        query = db.Indexed.find({}, {'Background':'1', 'Causes':'1', 'Symptoms':'1', 'Tips':'1'})
        for i in query:
            information.append((i['Background'], i['Causes'], i['Symptoms'], i['Tips']))

        return render_template('Cholera.html', diseases=diseases, information=information)

    @app.route('/typhoid')
    def typhoid():

        # get indexed diseases
        diseases = []
        information = []

        query = db.Diseases.find({}, {'Name':'1'})
        for i in query:
            diseases.append(i['Name'])

        query = db.Indexed.find({}, {'Background':'1', 'Causes':'1', 'Symptoms':'1', 'Tips':'1'})
        for i in query:
            information.append((i['Background'], i['Causes'], i['Symptoms'], i['Tips']))

        return render_template('Typhoid.html', diseases=diseases, information=information)

    @app.route('/malaria')
    def malaria():

        # get indexed diseases
        diseases = []
        information = []

        query = db.Diseases.find({}, {'Name':'1'})
        for i in query:
            diseases.append(i['Name'])

        query = db.Indexed.find({}, {'Background':'1', 'Causes':'1', 'Symptoms':'1', 'Tips':'1'})
        for i in query:
            information.append((i['Background'], i['Causes'], i['Symptoms'], i['Tips']))

        return render_template('Malaria.html', diseases=diseases, information=information)

except (Exception, errors):
    redirect(url_for('notFound'))
    
@app.route('/notFound')
def notFound():
    return jsonify(message='Cant Load This Page')

# execution
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)