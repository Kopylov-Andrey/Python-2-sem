from flask import Flask, render_template, url_for, redirect, request
import sqlalchemy as db




def searchdd(serchText):

    select_query = db.select(games).where(games.columns.name_game == serchText)
    select_result = connection.execute((select_query))
    searchGemas =select_result.fetchall()
    if len(searchGemas) ==0:
        select_query = db.select(games).where(games.columns.year == serchText)
        select_result = connection.execute((select_query))
        searchGemas = select_result.fetchall()
    return searchGemas


app = Flask(__name__)


try:
    engine = db.create_engine('mysql+pymysql://root:ason121245@localhost:3306/my_database')
    connection = engine.connect()
    print("Connect DB")
except Exception as ex:
    print("ERROR Connect DB")
    print(ex)

metadata = db.MetaData()
games = db.Table('games', metadata,
                 db.Column('game_id', db.Integer, primary_key=True),
                 db.Column('name_game', db.Text),
                 db.Column('year', db.Integer))

metadata.create_all(engine)

insertion_query = games.insert().values([
    {"name_game":"Minecraft", "year":2004},
    {"name_game":"Fortnite", "year":2006},
    {"name_game":"Grand Theft Auto V", "year":2020},
    {"name_game":"PUBG Mobile", "year":2010},
    {"name_game":"Overwatch", "year":2014},
    {"name_game":"League of Legends", "year":2001},
    {"name_game":"World of Warcraft", "year":2000},
    {"name_game":"Call of Duty: Modern Warfare", "year":2013},
    {"name_game":"The Witcher 3: Wild Hunt", "year":2016},
    {"name_game":"Assassin's Creed Origins", "year":2019},
    {"name_game":"FIFA 21", "year":2021},
    {"name_game":"Sims 4", "year":2002},
    {"name_game":"Borderlands 3", "year":2022},
    {"name_game":"Cyberpunk 2077", "year":2023},
    {"name_game":"Skyrim", "year":2003},
    {"name_game":"Rocket League", "year":2018},
    {"name_game":"Resident Evil 7", "year":2005},
    {"name_game":"Age of Empires II", "year":2017},
    {"name_game":"Hearthstone", "year":2007},
    {"name_game":"Cities: Skylines", "year":2015}
])
#connection.execute(insertion_query)

selall = db.select(games)
selres = connection.execute(selall)
allGames = selres.fetchall()

@app.route('/', methods =["GET", "POST"])
def index():
    if request.method == "POST":
        if request.form.get('clear') =='Clear':
            d = searchdd("s")
            return render_template('index.html', allGames=d, len=len(d))
        elif request.form.get('all') =='All List':
            render_template('index.html' , allGames = allGames, len = len(allGames))
        elif request.form.get('searchBtn') == 'Search':
            a = request.form.get("search")
            d = searchdd(a)
            return render_template('index.html' , allGames = d, len = len(d))
    return render_template('index.html' , allGames = allGames, len = len(allGames))

if __name__ == '__main__':
    app.run(debug=True, port=5001 )




