from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity,jwt_required

from . import bp as api
from app.models import Pokedex, Post, User

@api.post('/publish-post')
@jwt_required()
def publish_post():
    body = request.json.get('body')
    username = get_jwt_identity()
    user = User.query.filter_by(username=username).first()
    try:
      p = Post(body=body, user_id = user.user_id)
      p.commit()
    except:
       jsonify(message='Error Try Again'), 404
    return jsonify({
        'message': 'success post published',
        'logged_in_as' : username
        }), 200

@api.get('/user-posts/<username>')
@jwt_required()
def get_user_posts(username):
   user = User.query.filter_by(username=username).first()
   if not user:
      return jsonify({'message':'Invalid Username'}), 400
   user_posts = user.posts
   return jsonify({
      'message':'success',
      'posts': [{
         'body':post.body, 
         'timestamp':post.timestamp
         } for post in user_posts ]
   })

@api.delete('/delete-post/<post_id>')
@jwt_required()
def delete_post(post_id):
   post = Post.query.get(post_id)
   if not post:
      return jsonify(message='Invalid Post Id'), 400
   print(post.author)
   if post.author.username != get_jwt_identity():
      return jsonify(message='You cannont delete this post'), 400
   post.delete()
   return jsonify(message='Post Deleted')

@api.get('/user-profile/<username>')
def user_profile(username):
   user = User.query.filter_by(username = username).first()
   if user:
      return jsonify(user=user.to_dict())
   return jsonify(message='Invalid Username'), 404


@api.post('/add-to-pokedex')
@jwt_required()
def add_to_pokedex():
   poke_name = request.json.get('poke_name')
   poke_img = request.json.get('poke_img')
   username = get_jwt_identity()
   user = User.query.filter_by(username=username).first()
   try: 
      pd = Pokedex(
         poke_name = poke_name,
         poke_img = poke_img
      )
      pd.commit()
   except:
      jsonify(message='Error, could not add to Pokedex')
   return jsonify ({
      f'Success! {poke_name} has bbeen added to your pokedex!' 
   }), 200

@api.get('/pokedex/<username>')
@jwt_required()
def get_user_pokedex(username):
   user = User.query.filter_by(username = username).first()
   if not user:
      return jsonify({'message': 'Invalid username'}), 400
   user_pokedex = user.pokedex
   return jsonify({
      'message': 'success',
      'pokemon': [{
         'poke_name': pokedex.poke_name,
         'poke_img': pokedex.poke_img
      } for pokemon in user_pokedex]
   })

@api.delete('/delete/<poke_name>')
@jwt_required()
def delete_pokemon(poke_name):
   pokemon = Pokedex.query.get(poke_name)
   if not pokemon:
      return jsonify(message='Invalid pokemon'), 400
   if pokemon.trainer.username != get_jwt_identity():
      return jsonify(message="You cannot remove this pokémon"), 400
   pokemon.delete()
   return jsonify(message=f"{pokemon} has been removed from your pokedex")