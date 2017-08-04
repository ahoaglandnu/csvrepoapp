import sqlite3
from app import db 
conn = sqlite3.connect('csvtodbapp.db')
conn.close()
db.create_all()

print("""
Your sqlite database has been created.

You may now launch app.py
""")