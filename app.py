from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Kết nối database
def init_db():
    with sqlite3.connect("todo.db") as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS todos
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                         task TEXT NOT NULL,
                         done BOOLEAN NOT NULL DEFAULT 0)''')
        conn.commit()

# Route chính
@app.route('/')
def index():
    with sqlite3.connect("todo.db") as conn:
        todos = conn.execute('SELECT * FROM todos').fetchall()
    return render_template('index.html', todos=todos)

# Thêm task
@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    with sqlite3.connect("todo.db") as conn:
        conn.execute('INSERT INTO todos (task, done) VALUES (?, 0)', (task,))
        conn.commit()
    return redirect(url_for('index'))

# Đánh dấu task hoàn thành
@app.route('/complete/<int:id>')
def complete(id):
    with sqlite3.connect("todo.db") as conn:
        conn.execute('UPDATE todos SET done = 1 WHERE id = ?', (id,))
        conn.commit()
    return redirect(url_for('index'))

# Xóa task
@app.route('/delete/<int:id>')
def delete(id):
    with sqlite3.connect("todo.db") as conn:
        conn.execute('DELETE FROM todos WHERE id = ?', (id,))
        conn.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)