from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, unset_jwt_cookies

from . import bp as api
from app.models import User

@api.post('/register')
def register():
    content, response = request.json, {}
    print(content)
    if User.query.filter_by(email=content['email']).first():
        response['email error']=f'{content["email"]} is already taken. Please try again.'
    if User.query.filter_by(username=content['username']).first():
        response['username error']=f'{content["username"]} is already taken. Please try again.'
    if 'password' not in content:
        response['message']="Please include password"
    u=User()
    u.from_dict(content)
    try:
        u.hash_password(u.password)
        u.commit()
        return jsonify({'message': f'{u.username} is registered!'}, 200)
    except:
        return jsonify(response), 400
    
@api.post('sign-in')
def sign_in():
    username, password = request.json.get('username'), request.json.get('password')
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        access_token=create_access_token(identite=username)
        return jsonify({'access_token': access_token}), 200
    else:
        return jsonify({'message': 'Invalid username or password. Please try again.'}), 400
    
@api.post('/logout')
def logout():
    response = jsonify({'message':'You have successfully logged out.'})
    unset_jwt_cookies(response)
    return response

@api.delete('/delete-user/<username>')
@jwt_required()
def delete_user(username):
    password = request.json.get('password')
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        posts = user.posts
        for post in posts:
            post.delete()
        user.delete()
        return jsonify(message=f'{username} account deleted'), 200
    return jsonify(message="Invalid username and/or password"), 400