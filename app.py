import os
import sqlite3
from flask import Flask
from dotenv import load_dotenv

# Indlæs miljøvariabler fra .env fil
load_dotenv()
# comment
app = Flask(__name__)

# Hent miljøvariabler med standardværdier
GREETING_TYPE = os.getenv('GREETING_TYPE', 'default')
DB_PATH = os.getenv('DB_PATH', 'greetings.db')
SERVICE_URL = os.getenv('SERVICE_URL', 'http://example.com')

def get_message():
    # Opret database og tabel hvis de ikke findes
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Opret tabel hvis den ikke findes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS greetings
        (message TEXT NOT NULL)
    ''')
    
    # Tjek om tabellen er tom
    cursor.execute('SELECT COUNT(*) FROM greetings')
    if cursor.fetchone()[0] == 0:
        cursor.execute('INSERT INTO greetings (message) VALUES (?)', ['Hello, World!'])
        conn.commit()
    
    # Hent besked
    cursor.execute('SELECT message FROM greetings')
    message = cursor.fetchone()[0]
    
    conn.close()
    return message

@app.route('/')
def hello_world():
    return {
        'message': get_message(),
        'greeting_type': GREETING_TYPE,
        'service_url': SERVICE_URL
    }

if __name__ == '__main__':
    app.run()
