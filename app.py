
from flask import Flask, app, render_template

app = Flask(__name__)
app.jinja_env.cache = {}

@app.route("/")
def index():
  return render_template("index.html", message="nothing")

if __name__ == "__main__":
  app.run()