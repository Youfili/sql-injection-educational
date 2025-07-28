'''
Script che inizializza il DB
'''
import psycopg2

try:
    conn = psycopg2.connect(
        dbname="sqlinjection_db",
        user="ryan",
        password="prova",  # sostituisci con la tua password
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()

    with open('schema.sql', 'r') as f:
        sql_commands = f.read().split(';')  # divide i comandi SQL
        for command in sql_commands:
            if command.strip():  # ignora righe vuote
                try:
                    cur.execute(command + ';')
                except Exception as e:
                    print(f"\nErrore durante l'esecuzione del comando:\n{command.strip()}")
                    print(f"Errore: {e}\n")
                    conn.rollback()
                else:
                    conn.commit()

    cur.close()
    conn.close()
    print("Inizializzazione completata.")

except Exception as e:
    print(f"Errore di connessione: {e}")
