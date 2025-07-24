from flask import Flask, render_template, request, redirect, flash
import sqlite3  

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necessaria per i messaggi flash

@app.route('/')
def index():
    return render_template('index.html')  # home page

@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username'] 
        passwd = request.form['password']
        em = request.form['email']

        try:
            connection = sqlite3.connect('database.db')
            cursor = connection.cursor()

            # Query volutamente VULNERABILE per testare SQLi
            query = f"INSERT INTO users (username, password, email) VALUES ('{username}', '{passwd}', '{em}')"
            cursor.execute(query)
            connection.commit()

            flash("✅ Utente inserito con successo!", "success")

        except sqlite3.IntegrityError as e:
            if "username" in str(e).lower():
                flash("❌ Username già in uso! Provane un altro :)", "danger")
            elif "email" in str(e).lower():
                flash("❌ Email già registrata! Prova con un'altra :)", "danger")
            else:
                flash("❌ Errore durante la registrazione.", "danger")

        finally:
            connection.close()

        return redirect('/register')

    return render_template('register.html')

@app.route('/utenti', methods=('GET',))
def utenti():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    connection.close()

    return render_template('utenti.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)



