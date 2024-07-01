# To-do-using-flask
Responsive To-do Application in python using Flask Framework
## Features
- Add new to-do activities
- Update existing to-do activities
- Delete to-do activities
## Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.x
- MySQL server
## Getting Started
### Clone the Repository
```sh
git clone https://github.com/yourusername/flask-todo-app.git
cd flask-todo-app
```
### Install Dependencies
pip install -r requirements.txt
### MySQL Database Setup
1. Start your MySQL server.
2. Create a new database called flask:
```sql
CREATE DATABASE flask;
```
3. Create a table called todo:
```sql
USE flask;
CREATE TABLE todo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    activity VARCHAR(255) NOT NULL
);
```
4. Update the MySQL connection details in the app.py file if necessary:
```sql
connection = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="yourpassword", 
    database="flask"
)
```
### Run the Flask application using the following command:
```sh
flask run
```
## Project Structure
```graphql
flask-todo-app/
│
├── static/
│   ├── edit_todo.css
│   └── todo.css
│
├── templates/
│   ├── edit_todo.html
│   └── todo.html
│
├── .gitignore
├── README.md
├── app.py
└── requirements.txt

```
## Screenshot
![image](https://github.com/Jahnavi-57/To-do-using-flask/assets/130915370/4d1bcfca-3726-4f5a-a637-3d6f339892e2)
## Languages and Frameworks used:
<img  src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"/>
