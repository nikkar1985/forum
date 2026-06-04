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
