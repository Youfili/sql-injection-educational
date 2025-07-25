from flask import Flask, render_template, request, redirect, flash, session
import sqlite3  

app = Flask(__name__, template_folder='templates')
app.secret_key = 'supersecretkey'  # Necessaria per i messaggi flash e per session

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


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        em = request.form['email']
        passwd = request.form['password']

        # Ricerco all'interno del database se esiste una persona registrata con queste credenziali
        try: 
            connection = sqlite3.connect('database.db')
            cursor = connection.cursor()

            # QUERY più SICURA
            """
            query = "SELECT * FROM Users WHERE email = ? AND password = ?"
            cursor.execute(query, (em, passwd))
            """

            # realizzo la query di ricerca --> VULNERABILE
            query = f"SELECT * FROM Users WHERE email= '{em}' AND password='{passwd}'"
            cursor.execute(query)   

            # controllo se l'utente con queste credenziali esiste nel database:
            user = cursor.fetchone()
            if user:
                session['user_id'] = user[0]    #salvo l'ID utente nella sessione
                session['username'] = user[1]   # salvo anche l'username dell'utente nella sessione

                flash("✅ Ti sei loggato con successo!", "success")
                # mi dirigo verso la schermata dashboard di questo utente che si è appena loggato
                return redirect(f"/dashboard/{session['username']}")


            else:
                flash("❌ Email o Password Errati.", "danger")

        except sqlite3.Error as e:

            flash("❌ Errore generico del database.", "danger")

        finally:
            connection.close()

        return redirect('/login')

    return render_template('login.html')        # Renderizzo la pagina html del login




@app.route('/dashboard/<username>', methods=['GET'])    # dashboard del singolo utente per vedere le sue informazioni
def dashboard(username):

    if 'user_id' not in session or 'username' not in session:
        flash("❌ Devi effettuare il login per accedere alla dashboard.", "warning")
        return redirect('/login')
    
    # Faccio un controllo affinchè venga verificato che 'username' sia uguale a session['username']
    # Cosi un utente non può digitare /dashboard/mario se è loggato come luigi
    if session['username'] != username:
        flash("⛔ Accesso negato: non puoi visualizzare la dashboard di un altro utente!", "danger")
        return redirect('/login')



    # ricavo l'user direttamente dalla sessione attiva
    user_id = session.get('user_id')

    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Users WHERE id = ?", (user_id, )) # mi ricavo l'utente con questo id
    user = cursor.fetchone()

    connection.close()
    
    return render_template('dashboard.html', user=user)


@app.route('/logout')
def logout():
    session.clear()     # libero la sessione attuale
    flash("👋 Logout effettuato correttamente!", "info")
    return redirect('/')


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



