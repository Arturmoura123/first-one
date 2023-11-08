from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from os import environ


app = Flask(__name__)
app.config['SECRET_KEY'] = '12FRIENDS_FEEDBACK12'


# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///friends_feedback.db'
db = SQLAlchemy()
db.init_app(app)


class User(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True)
    feedback = Column(Text)


with app.app_context():
    db.create_all()



@app.route("/")
def root():
    return redirect("/index.html")


@app.route("/despedida.html")
def despedida_page():
    return render_template("despedida.html")


@app.route("/index.html")
def inicial_page():
    return render_template("index.html")


@app.route("/thefeedback.html")
def page_submit_feedback():
    return render_template("thefeedback.html")


@app.route("/submit-feedback", methods=["POST"])
def submit_feedback():
    name = request.form.get("name")
    feedback = request.form.get("feedback")

    new_feedback = User(name=name, feedback=feedback)
    db.session.add(new_feedback)
    db.session.commit()

    print(f"Nome: {name} \n"
          f"feedback: {feedback}")

    return redirect("despedida.html")





if __name__ == "__main__":
    app.run(debug=True)



