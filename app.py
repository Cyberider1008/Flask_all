from flask import Flask, render_template, request, redirect, url_for,flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = '1234'
db = SQLAlchemy(app)

#model for database
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable =True)
    email = db.Column(db.String(100), unique = True, nullable= False)

#create database table
with app.app_context():
    db.create_all()

#home route read data
@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users =users)

#create user
@app.route('/add', methods = ['GET', 'POST'])
def add_user():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        new_user = User(name = name, email=email)
        db.session.add(new_user)
        db.session.commit()
        flash("user add succesufully!", "success")
        return redirect(url_for('index'))
    return render_template("add.html")

#update user
@app.route('/edit/<int:id>', methods = ['GET', 'POST'])
def edit_user(id):
    user = User.query.get(id)
    if request.method == "POST":
        user.name = request.form['name']
        user.email = request.form['email']
        db.session.commit()
        flash("user update successfully!", "info")
        return redirect(url_for('index'))
    return render_template('edit.html', user = user)

#delete user
@app.route('/delete/<int:id>')
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    flash("user delete successfully!", "danger")
    return redirect(url_for("index"))

if __name__ == "__main__":

    app.run(debug=True)

