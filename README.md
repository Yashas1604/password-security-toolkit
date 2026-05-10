# 🔐 Password Cracking & Credential Security Toolkit

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20App-green)
![Security](https://img.shields.io/badge/Security-Ethical-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

> A practical web-based toolkit for password policy testing and 
> credential security assessment — built with Python & Flask.

---

## 📌 Project Overview

Weak passwords remain one of the most exploited vulnerabilities in 
cybersecurity. Attackers use dictionary attacks, credential dumping, 
and brute-force techniques to compromise systems.

This toolkit provides an **ethical, controlled environment** to understand:
- How password cracking works
- How credentials are stored as hashes
- How security teams can reinforce authentication mechanisms

---

## ✨ Features

| Module | Description |
|---|---|
| 💪 Password Strength Analyzer | Scores password strength across 7 security checks |
| 📖 Dictionary Generator | Generates wordlist variations from base words |
| 🔑 Hash Extractor | Simulates NTLM and SHA-512 hash extraction |
| 💥 Brute Force Simulation | Cracks short passwords using brute force |
| 📚 Dictionary Attack | Tests passwords against generated wordlist |

---

## 🛠️ Tech Stack

- **Backend:** Python 3, Flask
- **Frontend:** HTML, CSS, JavaScript
- **Security Concepts:** MD5, NTLM, SHA-512, Brute Force, Dictionary Attack

---

## ⚙️ How to Run Locally

### Prerequisites
- Python 3.10+
- pip

### Installation

**Step 1 — Clone the repository**
```bash
git clone https://github.com/Yashas1604/password-security-toolkit.git
cd password-security-toolkit
```

**Step 2 — Install dependencies**
```bash
pip install flask pyopenssl
```

**Step 3 — Run the app**
```bash
python app.py
```

**Step 4 — Open in browser**
