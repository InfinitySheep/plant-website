from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Making webpages load
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stats')
def statistics():
    conn = sqlite3.connect('database/sensor-data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT hour, light_level FROM light_readings")
    data = cursor.fetchall()
    conn.close()

    # Prepare data for plotting
    hours = [row[0] for row in data]
    levels = [row[1] for row in data]

    return render_template('statistics.html', hours=hours, levels=levels)

@app.route('/instructions')
def instructions():
    return render_template('instructions.html')

@app.route('/contact')
def contactUs():
    return render_template('contact-page.html')

# SQLite database initialization
def init_db():
    conn = sqlite3.connect('database/sensor-data.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS light_readings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        hour INTEGER NOT NULL,
        light_level REAL NOT NULL
    )
    ''')

    # Clear existing data
    cursor.execute('DELETE FROM light_readings')
    cursor.execute('DELETE FROM sqlite_sequence WHERE name="light_readings"')

    data = [
        (0, 0.0),
        (1, 3.7),
        (2, 0.0),
        (3, 1.5),
        (4, 0.0),
        (5, 12.9),
        (6, 35.2),
        (7, 60.7),
        (8, 72.4),
        (9, 85.6),
        (10, 90.1),
        (11, 95.8),
        (12, 99.2),
        (13, 97.5),
        (14, 89.0),
        (15, 78.3),
        (16, 65.4),
        (17, 45.0),
        (18, 30.8),
        (19, 15.2),
        (20, 8.4),
        (21, 4.1),
        (22, 2.0),
        (23, 0.5),
    ]

    cursor.executemany('''
    INSERT INTO light_readings (hour, light_level)
    VALUES (?, ?)
    ''', data)

    conn.commit()  # Save changes
    conn.close()

if __name__ == '__main__':
    init_db()          # Initialize the DB once when starting the app
    app.run(debug=True) # Enable debug mode with auto reload