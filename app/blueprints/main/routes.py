from flask import render_template, g
import random
from . import bp as main
from app.get_pokemon import RandomPokemon, Pokemon

@main.route('/')
def home():
    return render_template('index.jinja', title='Python Pokédex')

@main.route('/find_pokemon')
def find_pokemon():
    return render_template('find_pokemon.jinja', title='Find Pokémon')

# @main.route('/random_water_pokemon', methods=['POST'])
# def random_water_pokemon():
#     random_pokemon = RandomPokemon()
#     water_pokemon_list = Pokemon().WaterTypes()            
#     random_water_pokemon = random.choice(water_pokemon_list)
#     poke_water = Pokemon(random_water_pokemon)
#     return render_template('find_pokemon.jinja', random_pokemon=poke_water)