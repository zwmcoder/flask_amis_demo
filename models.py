from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Admin(db.Model):
    """用户表
    """
    id = db.Column(db.Integer, primary_key=True)
    admin = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(32), nullable=False)
    salt = db.Column(db.String(32), nullable=False)
    level = db.Column(db.Integer)
    name = db.Column(db.String(60), nullable=False)
    status = db.Column(db.Integer)

    def __init__(self, admin, password,salt,level,name,status):
    	self.admin=admin
    	self.password=password
    	self.salt=salt
    	self.level=level
    	self.name=name
    	self.status=status

    def __repr__(self):
        return '<id %r>' % self.id