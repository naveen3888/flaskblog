from flaskblog import app, db
from flaskblog.models import User

with app.app_context():
    user = User.query.first()
    print(user)
