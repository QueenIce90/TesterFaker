import os
from flask import Flask, make_response, g
from flask_migrate import Migrate
from models import db, User, Illness, Herbs

# Create a Flask application object
app = Flask(__name__)

# Configure a database connection to the local file app.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# Disable modification tracking to use less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration objects
db.init_app(app)
migrate = Migrate(app, db)

@app.before_request
def app_app():
    g.path = os.path.abspath(os.getcwd())

@app.route('/')
def index():
    response = make_response('<h1> Welcome To My Wellness Directory!</h1>', 200)
    return response

@app.route('/users')
def users():
    users = User.query.all()
    user_info = []
    for user in users:
        illness_info = [
            f"{illness.name} (Symptoms: {illness.symptoms}, Treatment: {illness.treatment})"
            for illness in user.illnesses
        ]
        user_info.append(f"{user.name}: {', '.join(illness_info)}")

    return '<h1>Welcome ' + ', '.join(user_info) + '</h1>'



@app.route('/treatment/<string:treatment>')
def illness_by_treatment(treatment):
    users = User.query.all()
    user_info = []
    for user in users:
        illness_info = [
            f"{illness.name}, Treatment: {illness.treatment})"
            for illness in user.illnesses
        ]
        user_info.append(f"{user.name}: {', '.join(illness_info)}")

    return '<h1> These are the herbs needed for these health conditions , ' + ', '.join (illness_info) +  '</h1>'


@app.route('/symptom/<string:symptom>')
def illness_by_symptom(symptom):
    illness_list = Illness.query.filter(Illness.symptoms.ilike(f'%{symptom}%')).all()
    
    size = len(illness_list)
    response_body = f'<h2> There {"is" if size == 1 else "are"} {size} illness{"es" if size != 1 else ""} associated with this symptom: {symptom} </h2>'
    for illness in illness_list:
        response_body += f'<h3> {illness.name} </h3>'
    response = make_response(response_body, 200)
    return response


    
@app.route('/illness')
def illnesses():
    illnesses = Illness.query.all()
    response_body = '<h1> Illnesses and Treatments </h1>'
    for illness in illnesses:
        response_body += f'''
            <h2> {illness.name} </h2>
            <h3> {illness.description} </h3>
            <h4> {illness.body_part} </h4>
            <h5> {illness.symptoms} </h5>
            <h6> {illness.treatment} </h6>
        '''
    response = make_response(response_body, 200)
    return response

@app.route('/herbs')
def herbs():
    herbs = Herbs.query.all()
    response_body = '<h1> Herbs </h1>'
    for herb in herbs:
        response_body += f'''
            <h2> {herb.name} </h2>
            <h3> {herb.description} </h3>
            <h4> {herb.health_benefits} </h4>
            <h5> {herb.side_effects} </h5>
            <h6> {herb.illness_id} </h6>
        '''

    response = make_response(response_body, 200)
    return response


@app.route('/about')
def about():
    return '<h1> About me </h1>'

@app.route('/contact')
def contact():
    return '''
        <h1> Contact me </h1>
        <a href="https://www.linkedin.com/in/sahil-kumar-singh-083a1217a/">LinkedIn</a>,
        <a href="https://github.com/sahilskumar">Github</a>,
        <a href="https://twitter.com/sahilskumar">Twitter</a>,
        <a href="https://www.facebook.com/sahil.kumar.singh.7">Facebook</a>,
        <a href="https://www.instagram.com/sahilskumar/">Instagram</a>,
        <a href="https://www.quora.com/profile/Sahil-Singh-2">Quora</a>,
        <a href="https://www.hackerrank.com/sahilskumar">HackerRank</a>,
        <h1> Email me at jaylynnbanos08@gmail.com <EMAIL> </h1>
        <h3> contact number +91 98100 47000 </h3>
        <h4> Do not call with the bullshit cause i will hang up the phone, its me Jaylynn!! </h4>
    '''

@app.route('/blog')
def blog():
    return '''
        <h1> Blog </h1>
        <h2> Learning How to Clean Your Ass Properly without leaving any SHIT STAINS!!!!
    '''

@app.route('/demo_json')
def demo_json():
    illness_json = '{"id": 1, "name" : "Diabetes", "treatment" : "Chamomile Tea, Orka"}'
    return make_response(illness_json, 200)

@app.route('/illness/<int:id>')
def illness_by_id(id):
    illness = Illness.query.filter_by(id=id).first()

    if illness:
        body = illness.to_dict()
        status = 200
    else:
        body = {'message': f'No illness with id {id}'}
        status = 404

    return make_response((body), status)

@app.route('/symptom/<string:symptom>')
def get_illness_by_symptom(symptom):
    illness_list = []  # List to store dictionaries for each illness
    
    # Query illnesses based on the symptom
    illnesses = Illness.query.filter_by(symptoms=symptom).all()
    
    # Build a dictionary for each illness
    for illness in illnesses:
        illness_dict = {
            'id': illness.id,
            'name': illness.name,
            'description': illness.description,
            'body_part': illness.body_part,
            'symptoms': illness.symptoms,
            'treatment': illness.treatment
        }
        illness_list.append(illness_dict.to_dict())
    
    # Prepare the response body
    response_body = {
        'count': len(illness_list),
        'illnesses': illness_list
    }
    # Return the response with a JSON format
    return make_response(response_body, 200)

@app.route('/username/<string:username>')
def get_user_by_username(username):
    username_list = []

    # Query users based on the username
    user = User.query.filter_by(username=username).all()

    # Build a dictionary for each user
    for user in user:
        username_dict = {
            'id': user.id,
            'username': user.username,
            'name': user.name,
            'email': user.email,
        }
        username_list.append(username_dict)

    # Prepare the response body
    response_body = {
        'count': len(username_list),
        'usernames': username_list
    }

    # Return the response with a JSON format
    return make_response(response_body, 200)

@app.route('/username/><string:username>')
def user_by_username(username):
    username_list = []

    # Query users based on the username
    user = User.query.filter_by(username=username).all()

    # Build a dictionary for each user
    for user in user:
        username_dict = {
            'id': user.id,
            'username': user.username,
            'name': user.name,
            'email': user.email,
        }
        username_list.append(username_dict)
        # Prepare the response body

        response_body = {
            'count': len(username_list),
            'usernames': username_list
        }
        

        # Return the response with a JSON format
        return make_response(response_body, 200)
    
        
@app.route('/email/<string:email>')
def get_user_by_email(email):
    email_list = []

    # Query users based on the email
    user = User.query.filter_by(email=email).all()

    # Build a dictionary for each user
    for user in user:
        email_dict = {
            'id': user.id,
            'username': user.username,
            'name': user.name,
            'email': user.email,
        }
        email_list.append(email_dict)

        # Prepare the response body
    response_body = {
            'count': len(email_list),
            'emails': email_list
        }
    # Return the response with a JSON format
    return make_response(response_body, 200)



if __name__ == '__main__':
    app.run(port=5555, debug=True)
