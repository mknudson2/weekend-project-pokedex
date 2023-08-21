import random
from random import randint, choice
from requests import get

class Pokemon:

    def __init__(self, name):
        self.name = name
        self.abilities = []
        self.weight = None
        self.types = []
        self.image = ''
        self.pokemon_api_call()
    
    def poke_api_call(self):
        res = get(f'https://pokeapi.co/api/v2/pokemon/{self.name}')
        if res.ok:
            data = res.json()
            self.name = data['name']
            self.abilities = data['abilities']
            self.weight = data['weight']
            self.types = data['types']
            self.image = data['sprites']['versions']['generation-v']['black-white']['animated']['front_shiny']
            if not self.image:
                self.image = data['sprites']['front_default']
            
        else:
            print(f"Error: status code {res.status_code}")

    
    def __repr__(self):
        return f'<Pokemon: {self.name}>'
    
    def display_poke_basic_info(self):
        print(f'{self.name}')
        print(f'Types: {self.types}')

    def display_image(self, width=150):
        print(f'<img src="{{ self.img}}" alt="{{ self.name }}" /> ')
        self.display_poke_basic_info()
    
    def WaterTypes(self):
        water_pokemon = []
        res = get('https://pokeapi.co/api/v2/pokemon/')  
        data = res.json()
        for pokemon_data in data['results']:
            pokemon_name = pokemon_data['name']
            res = get(pokemon_data['url']) 
            types = [t['type']['name'] for t in data['types']]
            if 'water' in types:
                water_pokemon.append(pokemon_name)



class RandomPokemon:
    
    def __init__(self):
        self.name = str(randint(1, 898)) #to generate a random pokemon and have it displayed, set the name to the random int as a string
        self.commentary = random.choice(("So cool!", "Nice!", "Way to go!", "No way?!", "...meh, I've seen better."))
    
    def poke_api_call(self):
        res = get(f'https://pokeapi.co/api/v2/pokemon/{self.name}')
        if res.ok: #if the request comes back a 200 (alright / good to go!)
            data = res.json() #we give the res(which is a var for accesssing our api), a new var with json conversion
            self.name = data['name'] #name is pulled from the data var (api info)
            self.image=data['sprites']['versions']['generation-v']['black-white']['animated']['front_shiny'] #image is pulled from the data var (api info)
            if not self.image: #in case animated image is not available for the int, an alternative is stated
                self.image = data['sprites']['front_default']
    
    def whos_that_pokemon(self):
        print('WHO\'S THAT POKEMON??')
        RandomPokemon.poke_api_call() #calls the api and images/names connected
        self.display_pokemon_image() #calls up the specific image for the random int pulled
        print(f'It\'s {self.name}! {self.commentary}') #calls up the associated name for that pokemon/image
        
    
    def display_pokemon_image(self, width=150):
        return self.image
    