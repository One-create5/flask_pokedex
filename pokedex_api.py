#!/usr/bin/env python3

from unicodedata import name
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
from flask import jsonify
import requests

app = Flask(__name__)

pokemondata = {}
id = 0

@app.route("/")
def start():
    return render_template("index.html")

@app.route("/validate", methods=["POST"])
def validate():
    if request.form.get("answer"):
        if request.method == "POST":
            userInput = request.form.get('answer').lower().strip()
            endpoint = f'https://pokeapi.co/api/v2/pokemon/{userInput}'
            res = requests.get(endpoint)
            if res.status_code == 200:
                res = res.json()
                game_name = res['name']
                game_index = res['game_indices'][3]['game_index']
                game_type = res['types'][0]['type']['name']
                game_weight = res['weight']
                game_height = res['height']
                game_image = res['sprites']['other']['official-artwork']['front_default']
            
         
                global id
                new_poke_data = {"index":game_index,"type": game_type,"weight":game_weight,"height":game_height,"image":game_image}
                pokemondata[game_name] = new_poke_data
                id += 1
                return redirect(url_for("success", name=game_name))
            else:
                return redirect(url_for("success", name="false"))
        else:
            return redirect(url_for("start"))
    else:
        return redirect(url_for("start"))

@app.route("/success/<name>/")
def success(name):
    return render_template("pokemonAdded.html", name=name)

@app.route("/api/v1")
def api():
    return jsonify(pokemondata)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)