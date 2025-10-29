# Progetto di Sicurezza Informatica – SQL Injection (SQLi)  

![Python](https://img.shields.io/badge/Python-3.10-blue) ![Flask](https://img.shields.io/badge/Flask-2.2-orange) ![License](https://img.shields.io/badge/License-MIT-green)  

[Download the project report (PDF)](docs/Sicurezza_Project.pdf)

---

## Project description
This project aims to provide a **hands-on demonstration of the main SQL Injection (SQLi) attack techniques** within web applications.  
The work was developed **for educational purposes** to understand how the vulnerability operates, its potential impacts, and possible mitigation strategies.  
Project developed for the Security course (Academic Year 2025), taught by Prof. Emiliano Casalicchio, as part of the Computer Science degree at “La Sapienza” University of Rome.

The project simulates an intentionally vulnerable web application with user authentication, allowing the testing of three specific attack techniques:
- Tautology
- EOL Comment
- PiggyBack Query

**Note:** Passwords in the database are stored in plain text for educational demonstration. In a real environment, passwords must be stored hashed and salted (e.g. bcrypt, Argon2).

---

## How to run the project

1. Clone the repository:
```bash
git clone https://github.com/Youfili/sql-injection-educational.git
```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
   
3. Start the application:
   ```bash
    python3 src/app.py
   ```

---

## Project report
The full PDF report includes:
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
