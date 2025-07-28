from flask import Flask, render_template, request, redirect, flash, session, url_for
import psycopg2
from datetime import datetime
import re

"""
Per Hashing password, OMESSA per fini Didattici

from werkzeug.security import generate_password_hash
"""

app = Flask(__name__, template_folder='templates')
app.secret_key = 'supersecretkey'  # Necessaria per i messaggi flash e per session

# Funzione di connessione al database PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        dbname="sqlinjection_db",
        user="ryan",
        password="prova",
        host="localhost",
        port="5432"
    )
    return conn


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        passwd = request.form['password']
        conf_passwd = request.form['confirm_password']
        em = request.form['email']
        gend = request.form['gender']
        phone = request.form.get('phone', '')
        bday = request.form['birthdate']
        terms = request.form.get('terms')
        priv = request.form.get('privacy')
        """
        NOTA: se l'utente non spunta il checkbox, quei campi non sono inviati nel form e questo solleverebbe un KeyError su request.form['terms'].
                Quindi è meglio usare .get()
        """



        # Controllo se password e confirm_password sono Uguali
        if passwd != conf_passwd:
            flash("Le password NON coincidono.")
            return redirect(url_for('register'))

        # Controllo Termini e Privacy
        if not terms or not priv:
            flash("Devi accettare i termini di servizio e la privacy policy per poterti registrare.")
            return redirect(url_for('register'))

    
        # Username: Lunghezza e caratteri consentiti (lettere, numeri, underscore)
        if not (3 <= len(username) <= 20) or not re.match(r'^\w+$', username):
            flash("❌ Lo username deve essere tra 3 e 20 caratteri e contenere solo lettere, numeri o underscore.", "danger")
            return redirect(url_for('register'))

        # Password:  almeno 8 caratteri, almeno un numero e un carattere speciale
        if len(passwd) < 8 or not re.search(r'\d', passwd) or not re.search(r'\W', passwd):
            flash("❌ La password deve avere almeno 8 caratteri, un numero e un carattere speciale.", "danger")
            return redirect(url_for('register'))
        
        # Email: validazione regex server side (molto base)
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_regex, em):
            flash("Email non valida.", "danger")
            return redirect(url_for('register'))


        # Telefono: validazione
        if phone and not re.fullmatch(r'[1-9][0-9]{9}', phone):
            flash("Numero di telefono non valido.", "danger")
            return redirect(url_for('register'))

        # Data di Nascita --> deve essere Maggiorenne
        try:
            nascita = datetime.strptime(bday, "%Y-%m-%d")
            oggi = datetime.today()
            anni = oggi.year - nascita.year - ((oggi.month, oggi.day) < (nascita.month, nascita.day))
            if anni < 18:
                flash("❌ Devi avere almeno 18 anni per registrarti.", "danger")
                return redirect(url_for('register'))
        except ValueError:
            flash("❌ Data di nascita non valida.", "danger")
            return redirect(url_for('register'))
        
        # Termini e Privacy
        if not terms or not priv:
            flash("Devi accettare i termini di servizio e la privacy policy per poterti registrare.")
            return redirect(url_for('register'))

        terms_accepted = True if terms else False
        privacy_accepted = True if priv else False


        """
        Hashing della password OMESSA per fini Didattici

        # Hash della password prima di salvare
        hashed_passwd = generate_password_hash(passwd)
        """

        # Connessione al DB
        connection = get_db_connection()
        cursor = connection.cursor()

        try:
            cursor.execute("""
                INSERT INTO users (username, password, email, gender, phone, birthdate, terms_accepted, privacy_accepted)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (username, passwd, em, gend, phone, bday, terms_accepted, privacy_accepted))

            connection.commit()
            flash("✅ Utente registrato con successo!\n Ora fai il login :)", "success")
            return redirect('/login')

        except Exception as e:
            if "username" in str(e).lower() and "unique" in str(e).lower():
                flash("❌ Username già in uso! Provane un altro :)", "danger")
            elif "email" in str(e).lower() and "unique" in str(e).lower():
                flash("❌ Email già registrata! Prova con un'altra :)", "danger")
            elif "phone" in str(e).lower() and "unique" in str(e).lower():
                flash("❌ Telefono già registrato! Prova con un altro :)", "danger")
            else:
                flash(f"❌ Errore durante la registrazione: {str(e)}", "danger")

        finally:
            cursor.close()
            connection.close()

        return redirect(url_for('register'))

    return render_template('register.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.clear()
        em = request.form['email']
        passwd = request.form['password']

        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (em, passwd))
            user = cursor.fetchone()

            """
            if user and check_password_hash(user[2], passwd):  # la password hashata è al campo index 2
            """

            if user:
                session['user_id'] = user[0]
                session['username'] = user[1]
                flash("✅ Ti sei loggato con successo!", "success")
                return redirect(f"/dashboard/{session['username']}")
            else:
                flash("❌ Email o Password Errati.", "danger")

        except Exception as e:
            flash(f"❌ Errore del database: {str(e)}", "danger")

        finally:
            connection.close()

        return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/dashboard/<username>', methods=['GET'])
def dashboard(username):
    if 'user_id' not in session or 'username' not in session:
        flash("❌ Devi effettuare il login per accedere alla dashboard.", "warning")
        return redirect(url_for('login'))

    if session['username'] != username:
        flash("⛔ Accesso negato: non puoi visualizzare la dashboard di un altro utente!", "danger")
        return redirect('/login')

    user_id = session.get('user_id')
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    connection.close()

    return render_template('dashboard.html', user=user)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/delete_account', methods=['POST'])
def delete_account():
    if 'user_id' not in session:
        flash("❌ Devi essere loggato per poter eliminare l'account.", "danger")
        return redirect(url_for('login'))

    user_id = session['user_id']
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    connection.commit()
    connection.close()
    session.clear()
    return redirect(url_for('index'))


@app.route('/utenti', methods=('GET',))
def utenti():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    connection.close()
    return render_template('utenti.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)
