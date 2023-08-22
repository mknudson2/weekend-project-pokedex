from random import choice
from flask import render_template, redirect, flash, url_for,g
from flask_login import current_user, login_required
import requests
from app import app
from app.forms import PokeForm, PostForm, UserSearchForm
from app.models import Post, User
from . import bp as social

@app.before_request
def before_request():
    g.search_form = UserSearchForm()
    g.post_form = PostForm()

@social.post('/post')
def post():
    if g.post_form.validate_on_submit():
        post = Post(body=g.post_form.body.data, user_id = current_user.user_id)
        post.commit()
        flash('Posted', category='success')
    return redirect(url_for('social.profile', username = current_user.username))

@social.route('profile/<username>')
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first()
    if user:
        posts= user.posts
        print(user.posts)
        return render_template('profile.jinja', username=username, posts=posts)
    else:
        flash(f'{username} is not a valid username. Please try again')
        return redirect(url_for('main.home'))
    
@social.post('user-search')
def user_search():
    return redirect(url_for('social.profile', username=g.search_form.username.data))

@social.post('/poke-add')
def find_pokemon():
    poke_form = PokeForm()
    if poke_form.validate_on_submit():
        poke_name = poke_form.poke_name.data
        url = f"https://pokeapi.co/api/v2/type/{poke_name}" 
        res = requests.get(url)
        
        if res.ok:
            data = res.json()
            pokemon_name = data['name']
            pokemon_img = data['sprites']['versions']['generation-v']['black-white']['animated']['front_shiny']
    return render_template('find_pokemon.jinja', poke_form=poke_form)


