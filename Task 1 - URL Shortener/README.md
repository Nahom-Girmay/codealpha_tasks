# SnapURL — URL Shortener

A simple and modern URL shortener built with **Python, Flask, and SQLite**.

SnapURL accepts a long URL, generates a unique short code, stores the URL mapping in a database, and redirects users from the shortened URL to the original destination.

## 🚀 Features

* 🔗 Convert long URLs into short URLs
* 🔐 Generate unique short codes
* 🗄️ Store URL mappings using SQLite
* ↪️ Redirect short URLs to their original URLs
* 📱 Responsive and modern user interface
* ✨ Animated success/result interface
* 🌐 Flask backend with a dedicated API endpoint
* 🧩 Organized project structure

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **Flask-SQLAlchemy**
* **SQLite**
* **HTML**
* **CSS**

## 📁 Project Structure

```text
Task 1 - URL Shortener/
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   ├── result.html
│   └── ...
│
├── app.py
├── config.py
├── models.py
├── utils.py
├── requirements.txt
└── README.md
```

## ⚙️ How It Works

1. The user enters a long URL.
2. Flask receives the URL through the `/shorten` endpoint.
3. The application generates a random short code.
4. The database is checked to make sure the generated code is not already being used.
5. The URL and unique short code are stored in SQLite.
6. SnapURL returns the shortened URL.
7. When someone visits the shortened URL, Flask looks up the corresponding original URL.
8. The user is redirected to the original destination.

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/Nahom-Girmay/codealpha_tasks.git
```

Navigate to the project:

```bash
cd codealpha_tasks/Task 1 - URL Shortener
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## ▶️ Running the Application

Start the Flask application:

```bash
python app.py
```

Then open the local address shown in the terminal, usually:

```text
http://127.0.0.1:5000
```

## 🔌 API Endpoint

The application includes a Flask endpoint that accepts a long URL and generates a unique short code.

```text
POST /shorten
```

The URL is submitted through the form and processed by the Flask backend.

## 🗄️ Database

SnapURL uses **SQLite** with **Flask-SQLAlchemy** to store URL mappings.

Each stored record contains information such as:

* Original URL
* Generated short code

The SQLite database is intentionally excluded from GitHub through `.gitignore`.

## 📸 Screenshots

Screenshots of the application can be added here.

## 🔮 Future Improvements

Possible future improvements include:

* Custom short URLs
* URL expiration
* Click analytics
* QR code generation
* User accounts
* Deployment with a custom domain

## 🎓 Internship Project

This project was developed as **Task 1** of the CodeAlpha internship program.

Built as a practical project to learn and demonstrate:

* Flask backend development
* Database integration
* Routing and redirects
* API endpoint development
* HTML/CSS frontend development
* Git and GitHub workflow
