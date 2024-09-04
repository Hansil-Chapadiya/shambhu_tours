# Import Libraries
from flask import Flask, render_template
from flask_cors import CORS
from flask_mail import Mail
from Controller.login import login_bp
from Controller.sign_up import signup_bp
from Controller.display_tour import display_tour_bp
from Controller.display_video import display_video_bp
from Controller.display_hottour import display_hot_tour_bp
from Controller.add_tour import add_tour_bp
from Controller.add_video import add_video_bp
from Controller.search_tour import search_tour_bp
from Controller.display_single_tour import single_tour_bp
from Controller.delete_tour import delete_tour_bp
from Controller.parameter_config import params
from Controller.send_otp import send_otp_bp
from Controller.extention import init_extensions
from Controller.reset_password import reset_password_bp
from Controller.admin_signup import subadmin_signup_bp
from Controller.admin_login import admin_login_bp
from Controller.subadmin_login import subadmin_login_bp
from Controller.remove_subadmin import delete_subadmin_bp
from Controller.sendotpadmin import send_otp_admin_bp
from Controller.admin_reset_password import admin_reset_password_bp
from Controller.edit_subadmin import edit_subadmin_bp
from Controller.fetch_subadmin import display_subadmin_bp
from Controller.fetch_single_admin import single_admin_bp
from Controller.display_subadmin_tour import subadmin_tour_bp
from Controller.registration_entry import registration_bp
from Controller.registration_admin_display import display_registration_bp
from Controller.registration_subadmin_display import display_subadmin_registration_bp
from Controller.registration_user_display import display_user_registarion_bp
from Controller.checkusertoken import check_token_bp
from Controller.contact import contact_us_bp
from Controller.display_contact import display_contact_bp
from Controller.add_vehicle import add_vehicle_bp
from Controller.display_admin_vehicle import display_admin_vehicle_bp
from Controller.delete_vehicle import delete_vehicle_bp
from Controller.edit_vehicle import edit_vehicle_bp
from Controller.display_vehicle import display_vehicle_bp
from Controller.display_admin_vehicle_category import display_admin_vehicle_category_bp
from Controller.display_vehicle_category import display_vehicle_category_bp
from Model.db_init import init_app


# run on local server
local_server = params['local_server']

# app name connect with templates folder
app = Flask(__name__, template_folder='templates')

origins = ['http://example.com', 'http://localhost:3000','https://shambhu-tours.vercel.app/', '*']  # Add your desired origins here

#add cors
CORS(app, origins=origins)

# create secret key
app.secret_key = params['SECRET_KEY']

# used for mail sending
init_extensions(app)

# differentiate local or production server
if (local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
    app.config['SQLALCHEMY_POOL_SIZE'] = params['pool_size']
    app.config['SQLALCHEMY_POOL_TIMEOUT'] = params['pool_timeout']  # 20 minutes
    app.config['SQLALCHEMY_POOL_RECYCLE'] = params['pool_recycle']

# configure application with Mail
mail = Mail(app)


# initialize the db object with the app object
init_app(app)

# Home end point


@app.route("/")
def home():
    return render_template('index.html')


# Login end-point
app.register_blueprint(login_bp)

# sign_up end-point
app.register_blueprint(signup_bp)

# display_tour end-point
app.register_blueprint(display_tour_bp)

# display_video end-point
app.register_blueprint(display_video_bp)

# display_hot_tour end-point
app.register_blueprint(display_hot_tour_bp)

# display_single_tour end-point
app.register_blueprint(single_tour_bp)

# add_tour end-point
app.register_blueprint(add_tour_bp)

# add_video end-point
app.register_blueprint(add_video_bp)

# search_tour end-point
app.register_blueprint(search_tour_bp)

# delete_tour end-point
app.register_blueprint(delete_tour_bp)

# delete_subadmin end-point
app.register_blueprint(delete_subadmin_bp)

# sendotp end-point
app.register_blueprint(send_otp_bp)

# sendotpadmin end-point
app.register_blueprint(send_otp_admin_bp)

# resetpassowrd end-point
app.register_blueprint(reset_password_bp)

# resetpassowrdadmin end-point
app.register_blueprint(admin_reset_password_bp)

# admin_login end-point
app.register_blueprint(admin_login_bp)

# admin_sign_up end-point
app.register_blueprint(subadmin_signup_bp)

# subadmin_login end-point
app.register_blueprint(subadmin_login_bp)

# subadmin-tour end-poin
app.register_blueprint(subadmin_tour_bp)

# single_admin end-point
app.register_blueprint(single_admin_bp)

# subadmin_edit end-point
app.register_blueprint(edit_subadmin_bp)

# subadmin_display end-point
app.register_blueprint(display_subadmin_bp)

# registration_entry end-point
app.register_blueprint(registration_bp)

# registration_display end-point
app.register_blueprint(display_registration_bp)

# registration_display_subadmin end-point
app.register_blueprint(display_subadmin_registration_bp)

# registration_display_user_registration end-point
app.register_blueprint(display_user_registarion_bp)

# user auth token bp
app.register_blueprint(check_token_bp)

# contact end-point
app.register_blueprint(contact_us_bp)

# contact display_bp
app.register_blueprint(display_contact_bp)

# add vehicle_bp
app.register_blueprint(add_vehicle_bp)

# edit vehicle_bp
app.register_blueprint(edit_vehicle_bp)

# display admin vehicle_bp
app.register_blueprint(display_admin_vehicle_bp)

# display user vehicle
app.register_blueprint(display_vehicle_bp)

# delete user_vehicle
app.register_blueprint(delete_vehicle_bp)

# admin category vehicle
app.register_blueprint(display_admin_vehicle_category_bp)

# category_vehicle
app.register_blueprint(display_vehicle_category_bp)

if __name__ == '__main__':
    app.run(debug=True)
