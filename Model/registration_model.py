from Model.db_init import db


class Registration_table(db.Model):
    '''
        p_id,p_name,payment_status,payment_mode,no_of_travellers,mobile_no,isExpired,tour_id_fk,email_fkey
    '''
    p_id = db.Column(db.Integer, primary_key=True)
    p_name = db.Column(db.String(50), nullable=False)
    payment_status = db.Column(db.Integer, nullable=False)
    payment_mode = db.Column(db.Integer, nullable=False)
    no_of_travellers = db.Column(db.String(50), nullable=False)
    mobile_no = db.Column(db.Integer, nullable=False)
    isExpired = db.Column(db.Integer, nullable=False)
    tour_id_fk = db.Column(db.String(50), nullable=False)
    email_fkey = db.Column(db.String(50), nullable=False)


class Registration_table_master(db.Model):
    '''
         p_id,p_name,payment_status,payment_mode,no_of_travellers,mobile_no,isExpired,tour_id_fk,email_fkey
    '''
    p_id = db.Column(db.Integer, primary_key=True)
    p_name = db.Column(db.String(50), nullable=False)
    payment_status = db.Column(db.Integer, nullable=False)
    payment_mode = db.Column(db.Integer, nullable=False)
    no_of_travellers = db.Column(db.String(50), nullable=False)
    mobile_no = db.Column(db.Integer, nullable=False)
    isExpired = db.Column(db.Integer, nullable=False)
    tour_id_fk = db.Column(db.String(50), nullable=False)
    email_fkey = db.Column(db.String(50), nullable=False)

