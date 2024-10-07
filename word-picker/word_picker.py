from random import choice
from flask import Flask
app = Flask(__name__)
choices = ["Sheldon Cooper", "Leonard Hofstadter", "Penny", "Howard Wolowitz", "Rajesh Koothrappali", "Amy Farrah Fowler", "Bernadette Rostenkowski", "Stuart Bloom", "Beverly Hofstadter", "Mary Cooper", "Leslie Winkle", "Priya Koothrappali", "Barry Kripke", "Emily Sweeney", "Zack Johnson"]
@app.route("/")
def pick_word():
  return choice(choices)