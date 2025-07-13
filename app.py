'''
Il Server Flask
'''
from flask import Flask, render_template, request, redirect
import sqlite3  

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')   # ritorno il template e lo rendo visualizzabile 
     

@app.route('/register', methods=('GET', 'POST'))
def register(): 

    if request.method == 'POST':
        # metto i parametri passati in post con HTML dentro delle variabili locali
        username = request.form['username']
        passwd = request.form['password']
        em = request.form['email']

        connection = sqlite3.connect('database.db')   # mi collego al database
        cursor = connection.cursor()

        # Query volutamente VULNERABILE a SQL Injection
        query = f"INSERT INTO Users (username, password, email) VALUES ('{username}', '{passwd}', '{em}')"
        cursor.execute(query)

        '''
        # Query Sicurezza Aumentata
        query = f"INSERT INTO Users (username, password, email) VALUES (?,?,?)" 
        cursor.execute(query, (username, passwd, em) )   # eseguo la query con parametri le variabili locali presi dalal request
        '''

        connection.commit()
        connection.close()

        return redirect('/')
    return render_template('/register.html')


# Voglio fare un'altra pagina in cui visualizzo tutti gli utenti registrati in questo momento
@app.route('/utenti', methods=('GET',))
def utenti():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Users")
    users = cursor.fetchall()   # il risultato della query viene formattato in lista di ennuple

    connection.close()      # chiudo la connessione

    return render_template('utenti.html', users=users)
    


if __name__ == '__main__':
    app.run(debug=True)

