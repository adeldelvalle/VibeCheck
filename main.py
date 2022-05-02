from flask import Flask, render_template
import sqlite3
import spotify_conn as spot


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


app = Flask(__name__)


@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


@app.route("/forward/", methods=['POST'])
def connect_spotify():
    connection = spot.Spotify()
    results = connection.music
    return render_template('index.html', results=results)
