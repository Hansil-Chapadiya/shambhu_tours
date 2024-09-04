from Model.db_init import db

class Rent_vehicle(db.Model):
    '''
        sr_no,v_image,mobile_no_fk,category,isAvailable
    '''
    sr_no = db.Column(db.Integer, primary_key=True)
    v_image = db.Column(db.String(1000), nullable=False)
    mobile_no_fk = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(4), nullable=False)
    isAvailable = db.Column(db.Integer, nullable=False)


class Rent_vehicle_master(db.Model):
    '''
        sr_no,v_image,mobile_no_fk,category,isAvailable
    '''
    sr_no = db.Column(db.Integer, primary_key=True)
    v_image = db.Column(db.String(1000), nullable=False)
    mobile_no_fk = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(4), nullable=False)
    isAvailable = db.Column(db.Integer, nullable=False)