from flask import Flask, render_template, request, redirect
from urllib.parse import urlparse
from config import Config
from models import db, Url
from utils import generate_short_code

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/shorten", methods=["POST"])
def shorten():

    original_url = request.form.get("url", "").strip()
    #return original_url

    if not original_url:
       return "Please enter a URL", 400

    parsed_url = urlparse(original_url)

    if parsed_url.scheme not in ("http", "https") or not parsed_url.netloc:
       return "Invalid URL", 400

    existing_url = Url.query.filter_by(
       original_url = original_url
    ).first()

    if existing_url:
       return render_template(
          "result.html",
          short_code=existing_url.short_code,
          original_url=existing_url.original_url
       )

    while True:
       
        short_code = generate_short_code()

        existing = Url.query.filter_by(
            short_code=short_code
        ).first()

        if existing is None:
            break 


    new_url = Url(
        original_url = original_url,
        short_code = short_code
    )

    db.session.add(new_url)
    db.session.commit()

    return render_template(
       "result.html",
       short_code=short_code,
       original_url=original_url
    )

@app.route("/<short_code>")
def redirect_to_url(short_code):

    url = Url.query.filter_by(short_code=short_code).first()

    if url is None:
       return render_template("404.html"), 404

    return redirect(url.original_url)


app.config.from_object(Config)

db.init_app(app) 

if __name__ == "__main__":

  with app.app_context():
    db.create_all()

  app.run(debug=True)