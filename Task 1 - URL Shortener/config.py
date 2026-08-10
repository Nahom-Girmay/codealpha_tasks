# For Database purpose

import os    # Python's built-in os module to work with file paths

BASE_DIR = os.path.abspath(os.path.dirname(__file__)) # This finds the absolute path of your project folder.

class Config:

  SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "instance", "urls.db") # point SQLAlchemy to the SQLite database file.

  SQLALCHEMY_TRACK_MODIFICATIONS = False 