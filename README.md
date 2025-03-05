# Flask_all
# Flask CRUD App

This is a simple **CRUD (Create, Read, Update, Delete) application** built using **Flask** and **SQLite**. It allows users to manage a list of users with basic operations.

## Features
- **Create** new users
- **Read** and list all users
- **Update** existing user details
- **Delete** users from the database

## Technologies Used
- Flask (Python web framework)
- SQLite (Database)
- SQLAlchemy (ORM for database interactions)
- HTML/CSS (for frontend templates)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Cyberider1008/Flask_all.git
cd flask_all
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate 
```

### 3. Install Dependencies
```bash
pip install flask flask-sqlalchemy flask-wtf wtforms
```

### 4. Run the Application
```bash
python app.py
```

### 5. Open in Browser
```
http://127.0.0.1:5000/
```

## Project Structure
```
flask_crud_app/
│── app.py  # Main Flask application
│── templates/
│   ├── index.html  # Home page with user list
│   ├── add.html    # Form to add a new user
│   ├── edit.html   # Form to update user details
│── database.db  # SQLite database (auto-created)
│── static/  # (Optional for CSS/JS files)
```

## Usage
1. **Home Page:** Displays a list of users.
2. **Add User:** Click "Add User" to enter name and email.
3. **Edit User:** Click "Edit" next to a user to update their details.
4. **Delete User:** Click "Delete" to remove a user from the database.


