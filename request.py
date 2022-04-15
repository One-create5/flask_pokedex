#!/usr/bin/env python3

from pydoc import plain
import requests

endpoint = 'http://localhost:8000/api/v1'

def main():
    
    pokemon = requests.get(endpoint).json()

    print("Pokemon STATS")
    for pokeinfo in pokemon:
        print("*************************")
        print(f"*   Name: {pokeinfo} \t*")
        print(f"*   Height: {pokemon[pokeinfo]['height']}\t\t*")
        print(f"*   Weight: {pokemon[pokeinfo]['weight']}   \t*")
        print(f"*   Index: {pokemon[pokeinfo]['index']}\t\t*")
        print(f"*   Type: {pokemon[pokeinfo]['type']}   \t*")
        print("*************************", end='\n\n')

if __name__ == "__main__":
    main()