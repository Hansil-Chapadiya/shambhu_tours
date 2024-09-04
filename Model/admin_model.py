from Model.db_init import db


class Admin(db.Model):
    '''
        sr_no,email,mobile_no,password,username,role,states
    '''
    sr_no = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    mobile_no = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    states = db.Column(db.String(50), nullable=False)
    role = db.Column(db.Integer, nullable=False)


class Admin_master(db.Model):
    '''
        sr_no,email,mobile_no,password,username,role,states
    '''
    sr_no = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    mobile_no = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    states = db.Column(db.String(50), nullable=False)
    role = db.Column(db.Integer, nullable=False)
