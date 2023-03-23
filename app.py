from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient('localhost', 27017)

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method=='POST':

        title = request.form['title']
        hyperautomation = request.form['hyperautomation']
        serialnumber = request.form['serialnumber']
        email = request.form['email']
        sql_query = request.form['sql_query']

        projects.insert_one(
            {
                'title': title, 
                'hyperautomation': hyperautomation,
                'serialnumber': serialnumber,
                'email':email,
                'sql_query':sql_query
            }
        )
        
        return redirect(url_for('index'))

    all_projects = projects.find()
    return render_template('project_forms.html', projects=all_projects)


@app.post('/<id>/delete/')
def delete(id):
    projects.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))

db = client.flask_db
projects = db.projects