from CMS import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    fullname = db.Column(db.String(120), nullable=False)
    phonenumber = db.Column(db.Integer,nullable=False)
    address = db.Column(db.String(200))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    country = db.Column(db.String(50))
    pincode = db.Column(db.Integer, nullable=False)
    userposts = db.relationship('Content',backref='author',lazy=True)

    def __repr__(self):
        return f"User ('{self.email}','{self.fullname}','{self.phonenumber}')"



#
class Content(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    body = db.Column(db.String(300), nullable=False)
    summary = db.Column(db.String(60), nullable=False)
    document =  db.Column(db.String(20), nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)
    tags= db.Column(db.String(20))


    def __repr__(self):
        return f"Content ('{self.title}','{self.author}','{self.tags}')"
