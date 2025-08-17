# Progetto di Sicurezza Informatica – SQL Injection (SQLi)  

![Python](https://img.shields.io/badge/Python-3.10-blue) ![Flask](https://img.shields.io/badge/Flask-2.2-orange) ![License](https://img.shields.io/badge/License-MIT-green)  

[Scarica la relazione del progetto in PDF](docs/relazione.pdf)

---

## Descrizione del progetto
Questo progetto ha come obiettivo la **dimostrazione pratica delle principali tecniche di attacco SQL Injection** (SQLi) all’interno di applicazioni web.  
L’attività è stata sviluppata **a scopo didattico**, per comprendere il funzionamento della vulnerabilità, i suoi effetti e le possibili strategie di mitigazione.

Progetto sviluppato per il corso di Sicurezza (Anno Accademico 2025), tenuto dal Prof. Emiliano Casalicchio, nell’ambito del Corso di Laurea in Informatica presso l’Università “La Sapienza” di Roma.

Il progetto simula un’applicazione web con autenticazione utente intenzionalmente vulnerabile, permettendo di testare tre tecniche specifiche di attacco:
- Tautologia
- EOL Comment
- PiggyBack Query

**Nota:** le password nel database sono lasciate in chiaro per motivi didattici. In un contesto reale dovrebbero essere memorizzate in forma hashata con salatura (bcrypt, Argon2).

---

## Come eseguire il progetto

1. Clona il repository:
```bash
git clone https://github.com/tuo-profilo/tuo-repo.git
```
2. Installa le dipendenze:
    ```bash
    pip install -r requirements.txt
    ```
   
3. Avvia l’applicazione:
   ```bash
    python3 src/app.py
   ```

4. Apri il browser e accedi a http://localhost:5000 per testare l’applicazione.

---

## Relazione del progetto
La relazione completa in PDF include:
- Introduzione teorica alla SQL Injection
- Tecniche di attacco utilizzate
- Analisi dei rischi
- Strategie di mitigazione
- Esempi di codice

## Strumenti utilizzati
- Linguaggio: Python 3.x
- Framework web: Flask
- Template engine: Jinja2
- Database: PostgreSQL
- Front-end: HTML5, CSS3, Bootstrap 5, JavaScript
- Gestione sessioni: Flask-Session
- Sistema operativo di sviluppo: Ubuntu 22.04

## Note aggiuntive
- Il progetto è a **scopo didattico**, non per utilizzo in ambienti reali
- La sicurezza delle password è volutamente compromessa per dimostrare le vulnerabilità SQLi
- Eventuali miglioramenti futuri possono includere:
  - Hashing sicuro delle password (bcrypt, Argon2)
  - Logging avanzato delle query
  - Filtraggio e validazione più robusta degli input utente
    
---
