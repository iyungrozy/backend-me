import os

from app import create_app
from app.models.user import User
from app.data_models.user import UserData
from app.extensions import db

app = create_app('prod')
db.app = app

db.create_all()
db.session.commit()

user = db.session.query(User).filter(User.is_admin == True).first()

if user is None:
    user = User(UserData(os.getenv("USERNAME", "admin"), os.getenv("PASSWORD", "admin"), os.getenv("EMAIL", "admin"), True))
    user.add(user)
    print("Administrator account has been created")

if __name__ == "__main__":
    app.run()
