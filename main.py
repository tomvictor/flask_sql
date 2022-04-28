from flask import Flask

from flask_migrate import Migrate
from flask_script import Manager


from config import Config
from logic import db_query
from models import db

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)
manager = Manager(app)





@app.route("/")
def hello_world():
    return db_query()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port= 8080)
