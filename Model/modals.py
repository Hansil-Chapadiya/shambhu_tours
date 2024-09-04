from Model.db_init import db

class Login(db.Model):
    '''
        sr_no,email,password,username
    '''
    sr_no = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(50),nullable=False)
    username = db.Column(db.String(50),nullable=False)

