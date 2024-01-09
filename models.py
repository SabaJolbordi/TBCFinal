from ext import db, app, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
# from models import Product


from ext import db  # Assuming 'ext' is the SQLAlchemy instance
# db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    maintitle = db.Column(db.String(255), nullable=False)
    img = db.Column(db.String(255), nullable=False)
    card_title = db.Column(db.String(255), nullable=False)
    time = db.Column(db.String(255), nullable=False)
    # role = db.Column(db.String)
    # likes = db.Column(db.Integer, default=0)




    def __repr__(self):

        return f"<Product {self.maintitle}>"


class BaseModel:
    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def save(self):
        db.session.commit()



class User(db.Model, BaseModel, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    # role = db.Column(db.String)
    # role = db.Column(db.String(20), nullable=False, default='user')

    def __init__(self, username,password):
        # role = "guest"
        self.username = username
        self.password = generate_password_hash(password)
        # self.role = role

        # def check_password(self, password):
        #     return check_password_hash(self.password, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()


        # new_user = User(username="admin_user", password="password", role="admin")
        # new_user.create()
