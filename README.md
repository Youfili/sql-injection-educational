# Web Application Security Project – SQL Injection (SQLi)

![Python](https://img.shields.io/badge/Python-3.10-blue) 
![Flask](https://img.shields.io/badge/Flask-2.2-orange) 
![License](https://img.shields.io/badge/License-GNU%20GPL%20v3.0-green)  
[![Contribute](https://img.shields.io/badge/Contribute-Welcome-brightgreen)](https://github.com/Youfili/sql-injection-educational/pulls) 
[![Collaboration](https://img.shields.io/badge/Collaboration-Open-blue)](https://github.com/Youfili/sql-injection-educational/issues)

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
- Theoretical introduction to SQL Injection
- Attack techniques used
- Risk analysis
- Mitigation strategies
- Code examples

## Tools and technologies
- Language: Python 3.x
- Web framework: Flask
- Template engine: Jinja2
- Database: PostgreSQL
- Front-end: HTML5, CSS3, Bootstrap 5, JavaScript
- Session management: Flask-Session
- Development OS: Ubuntu 22.04

## Additional notes
- This project is for educational purposes only and should not be used in production environments.
- Password security is intentionally weakened to demonstrate SQLi vulnerabilities.
- Possible future improvements:
  - Secure password hashing (bcrypt, Argon2)
  - Advanced query logging and auditing
  - Stronger input validation and sanitization
  - Parameterized queries / prepared statements everywhere
  - Automated tests covering both normal and malicious inputs
    
---

Contributing

Contributions, suggestions and improvements are very welcome — whether it's code hardening, documentation, tests, or additional attack/defense scenarios. If you want to contribute:
    1) Fork the repository.
    2) Create a feature branch: git checkout -b feature/your-feature.
    3) Commit your changes and open a pull request describing the enhancement/fix.
Please open issues for bugs, security improvements, or documentation updates. When proposing security fixes, prefer opening a private communication channel if the fix relates to novel vulnerabilities that could be abused before patches are merged.

---

Ethical use & disclaimer

This repository is intended strictly for learning and research. Do not use the techniques demonstrated here against systems for which you do not have explicit authorization. Misuse of the materials in this repository for malicious purposes is strictly prohibited and may be unlawful.

---

Contact & collaboration

If you'd like to collaborate, report improvements, or discuss the project, feel free to:
    - Open an issue or pull request on GitHub
    - Send a short message in the repository’s issue tracker

I’m open to collaborations to:
    - Harden the application (implement secure coding practices)
    - Expand the report with more mitigations and tests
    - Add CI pipelines and automated security checks

Thank you for taking a look — contributions and constructive feedback are highly appreciated.

---
