from app import app, controller
from flask import jsonify, request
from flasgger import swag_from

@app.route('/games', methods=['GET'])
@swag_from('../docs/get_games.yaml')
def get_games():
    return jsonify(controller.get_games())

@app.route('/games/<game_id>', methods=['GET'])
@swag_from('../docs/get_single_game.yaml')
def get_game(game_id):
    return jsonify(controller.get_game_by_id(game_id))

@app.route('/games/add', methods=['POST'])
@swag_from('../docs/add_game.yaml')
def add_game():
    game = request.get_json()
    name = game["name"]
    publisher = game["publisher"]
    rating = game["rating"]
    price = game["price"]
    year = game["year"]
    return jsonify(controller.add_game(name, publisher, rating, price, year))

@app.route('/games/update', methods=['PUT'])
@swag_from('../docs/update_game.yaml')
def update_game():
    game = request.get_json()
    return jsonify(controller.update_game(game))

@app.route('/games/delete/<game_id>', methods=['DELETE'])
@swag_from('../docs/delete_game.yaml')
def delete_game(game_id):
    return jsonify(controller.delete_game(game_id))