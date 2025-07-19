from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import sqlite3

app = Flask(__name__)

# DB setup
def init_db():
    with sqlite3.connect('tickets.db') as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS tickets (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            issue TEXT NOT NULL,
                            urgency TEXT,
                            status TEXT DEFAULT 'Open',
                            created_at TEXT
                        )''')

# Home Page / Form
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        issue = request.form['issue']
        urgency = request.form['urgency']
        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        with sqlite3.connect('tickets.db') as conn:
            conn.execute("INSERT INTO tickets (name, issue, urgency, created_at) VALUES (?, ?, ?, ?)",
                         (name, issue, urgency, created_at))
        return redirect(url_for('index'))

    with sqlite3.connect('tickets.db') as conn:
        tickets = conn.execute("SELECT * FROM tickets ORDER BY created_at DESC").fetchall()
    return render_template('index.html', tickets=tickets)

# Close ticket
@app.route('/close/<int:ticket_id>')
def close_ticket(ticket_id):
    with sqlite3.connect('tickets.db') as conn:
        conn.execute("UPDATE tickets SET status='Closed' WHERE id=?", (ticket_id,))
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
