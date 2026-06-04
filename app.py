import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name___)

DB_FILE = 'forum.db'


def get_db_connection():
  conn = sqlite3.connect(DB_FILE)
  conn.row_factory = sqlite3.Row
  return conn

def init_db():
  conn=get_db_connection()
  conn.execute('''CREATE TABLE IF NOT EXISTS posts(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   title TEXT NOT NULL,
   content TEXT NOT NULL,
   username TEXT NOT NULL,
   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
   ''')
  
  conn.execute(''' CREATE TABLE IF NOT EXISTS comments (
  id INTEGER PRIMARY KEY AUTOINCEMENT,
  post_id INTEGER NOT NULL,
  content TEXT NOT NULL,
  username TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY(post_id) REFERENCES posts (id))
  ''')
  conn.commit()
  conn.close()


init_(db)

@app.route('/')
def index():
  conn=get_db_connection()
  posts = conn.execute('SELECT * FROM posts ORDER BY created_at DESC').fetchall()
  conn.close()
  retun render_template('index.html', posts=posts)



@app.route('/create', methods=['POST'])
def create_post():
  title = requests.form.get('title')
  content = requests.form.get('content')
  username - requests.form.get('username') or 'Ανώνυμος'

if title and content:
  conn=get_db_connection()
  conn.exucute('INSERT INTO posts (title, content, username) VALUES (?, ?, ?)', (title,content, username))
  conn.commit()
  conn.close()
return redirect(url_for('index.html'))
  
  
@app.route('/post/<int::post_id', methods =['GET', 'POST'])
def view_oost(post_id):
  conn=get_db_connection()
  if requests.method == 'POST':
    content=request.form.get('content')
    username = request.form.get('username') or 'Ανώνυμος'
    if content:
      conn.execute('INSERT INTO comments(post_id, content, username) VALUES (?, ? , ?)',(post_id, content, username))
      conn.commit()
    
    
    
