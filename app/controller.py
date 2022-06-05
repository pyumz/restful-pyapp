from app.database import db_connect
from app import app
import sqlite3

def add_game(name, publisher, rating, price, year):
    game_added = {}

    database = db_connect()
    cursor = database.cursor()

    cursor.execute("INSERT INTO vgames(name, publisher, rating, price, year) VALUES(?, ?, ?, ?, ?)", (name, publisher, rating, price, year))
    database.commit()

    game_added = get_game_by_id(cursor.lastrowid)

    database.close()
    
    return game_added


def update_game(game):
    game_updated = {}
    try: 
        database = db_connect()
        cursor = database.cursor()

        update_statement = "UPDATE vgames SET name = ?, publisher = ?, rating = ?, price = ?, year = ? WHERE game_id=?"
        cursor.execute(update_statement, (game['name'], game['publisher'], game['rating'], game['price'], game['year'], game['game_id']))
        database.commit()

        
        game_updated = get_game_by_id(game["game_id"])
    except:
        database.rollback()
        print("Failed to update game, rolling back changes")
    finally:
        database.close()

    return game_updated

def get_games():
    game_list = []
    try: 
        database = db_connect()
        cursor = database.cursor()

        select_all_statement = "SELECT * from vgames"
        cursor.execute(select_all_statement)
        games = cursor.fetchall()
       
        for game in games:
            game_list.append(
                {
                    "game_id"   : game["game_id"],
                    "name"      : game["name"],
                    "publisher" : game["publisher"],
                    "rating"    : game["rating"],
                    "price"     : game["price"],
                    "year"      : game["year"],
                }
            )
        print("Game list retrieved!")
    except:
        game_list = []
    
    return game_list

def get_game_by_id(game_id):
        game = {}
        database = db_connect()
        database.row_factory = sqlite3.Row
        cursor = database.cursor()

        select_one_statement = "SELECT * FROM vgames WHERE game_id = ?"
        cursor.execute(select_one_statement, (game_id,))
        row = cursor.fetchone()
        game["game_id"] = row["game_id"],
        game["name"]    = row["name"],
        game["publisher"] = row["publisher"],
        game["rating"]    = row["rating"],
        game["price"]     = row["price"],
        game["year"]      = row["year"]

        return game

def delete_game(game_id):
        database = db_connect()
        cursor = database.cursor()

        cursor.execute("DELETE FROM vgames WHERE game_id = ?", [game_id])
        database.commit()
        print("Game deleted from Video Games database")

        database.rollback()

        database.close()
        return 

