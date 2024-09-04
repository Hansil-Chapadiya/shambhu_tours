from Model.db_init import db

class Contact_us(db.Model):
    '''
        sr_no,name,mobile_no,message
    '''
    sr_no = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    mobile_no = db.Column(db.Integer, nullable=False)
    message = db.Column(db.String(100), nullable=False)