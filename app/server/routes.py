from flask import request, jsonify, make_response

from app.server import app, bcrypt, db
from app.server.models import User


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/api/register', methods=['POST'])
def register():
    json_data = request.json
    user = User.query.filter_by(email=json_data.get('email')).first()
    if not user :
        try:
            user = User(
                email = json_data.get('email'),
                password = json_data.get('password')
            )

            #insert new user into db
            db.session.add(user)
            db.session.commit()

            auth_token = user.encode_auth_token(user.id)
            responseObject = {
                'status': 'success',
                'message': 'User successfully registered',
                'auth_token': auth_token.decode()
            }
            return make_response(jsonify(responseObject)), 200
        except Exception as e:
            print(e)
            responseObject = {
                    'status': 'failed',
                    'message': 'Internal Server Error. Please try again'
                }
            return make_response(jsonify(responseObject)), 500
    else:
        responseObject = {
                'status': 'failed',
                'message': 'User already exists. Please Log in.',
            }
        return make_response(jsonify(responseObject)), 200


@app.route('/api/login', methods=['POST'])
def login():
    json_data = request.json
    try:
        user = User.query.filter_by(email=json_data.get('email')).first()
        if user and bcrypt.check_password_hash(
                user.password, json_data.get('password')):
                auth_token = user.encode_auth_token(user.id)
                if auth_token:
                    responseObject = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'auth_token': auth_token.decode()
                    }
                    return make_response(jsonify(responseObject)), 200
        else:
            responseObject = {
                        'status': 'failed',
                        'message': 'User does not exist'
                    }
            return make_response(jsonify(responseObject)), 200 
    except Exception as e:
        print(e)
        responseObject = {
                    'status': 'failed',
                    'message': 'Internal Server Error. Please try again'
                }
        return make_response(jsonify(responseObject)), 500


@app.route('/api/logout')
def logout():
    auth_header = request.headers.get('Authorization')
    if auth_header:
        auth_token = auth_header.split(" ")[1]
    else:
        auth_token = ''
    if auth_token:
        resp = User.decode_auth_token(auth_token)
        if not isinstance(resp, str):
            responseObject = {
                    'status': 'success',
                    'message': 'Successfully logged out.'
                }
            return make_response(jsonify(responseObject)), 200
        else:
            responseObject = {
                    'status': 'failed',
                    'message': resp
                }
            return make_response(jsonify(responseObject)), 500
    else:
        responseObject = {
                'status': 'failed',
                'message': 'Error in logging out. Invalid token'
        }
        return make_response(jsonify(responseObject)), 401


@app.route('/api/status')
def status():
    auth_header = request.headers.get('Authorization')
    if auth_header:
        try:
            auth_token = auth_header.split(" ")[1]
        except IndexError:
            responseObject = {
                'status': 'fail',
                'message': 'Bearer token malformed.'
            }
            return make_response(jsonify(responseObject)), 401
    else:
        auth_token = ''
    if auth_token:
        resp = User.decode_auth_token(auth_token)
        if not isinstance(resp, str):
            user = User.query.filter_by(id=resp).first()
            responseObject = {
                'status': 'success',
                'data': {
                    'user_id': user.id,
                    'email': user.email,
                    'registered_on': user.registered_on
                }
            }
            return make_response(jsonify(responseObject)), 200
        responseObject = {
            'status': 'fail',
            'message': resp
        }
        return make_response(jsonify(responseObject)), 401
    else:
        responseObject = {
            'status': 'failed',
            'message': 'Provide a valid auth token.'
        }
        return make_response(jsonify(responseObject)), 401
