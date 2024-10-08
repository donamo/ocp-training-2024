from random import choice
from os import environ
from flask import Flask

app = Flask(__name__)

def load_options(file_path):
  with open(file_path, "r", encoding="utf-8") as f:
    file_contents = f.read()
  return file_contents.splitlines()

options = load_options(environ.get("OPTIONS_FILE", "options.txt"))

@app.route("/")
def pick_word():
  return choice(options)