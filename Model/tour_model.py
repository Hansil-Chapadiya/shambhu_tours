from Model.db_init import db

class Tours(db.Model):
    '''
        tour_id,title,description,image,video,day,night,rating,categories,price,states,hottour,isDisable,endReservation
    '''
    tour_id = db.Column(db.String(50), primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(2500), nullable=False)
    video = db.Column(db.String(3000), nullable=False)
    day = db.Column(db.Integer, nullable=False)
    night = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    categories = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float, nullable=False)
    states = db.Column(db.String(50), nullable=False)
    hottour = db.Column(db.Boolean, nullable=False)
    isDisable = db.Column(db.Integer, nullable=False)
    endReservation = db.Column(db.String(15), nullable=False)


class Tours_master(db.Model):
    '''
        tour_id,title,description,image,video,day,night,rating,categories,price,states,hottour,isDisable,endReservation
    '''
    tour_id = db.Column(db.String(50), primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(2500), nullable=False)
    video = db.Column(db.String(3000), nullable=False)
    day = db.Column(db.Integer, nullable=False)
    night = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    categories = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float, nullable=False)
    states = db.Column(db.String(50), nullable=False)
    hottour = db.Column(db.Boolean, nullable=False)
    isDisable = db.Column(db.Integer, nullable=False)
    endReservation = db.Column(db.String(15), nullable=False)
