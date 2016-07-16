import os
import re
from flask_mail import Mail, Message
from flask import flash,session,request,render_template,redirect,url_for,g,jsonify
from leaveapp import leaveapp,db,lm,oid
from .forms import RegistrationForm,LoginForm,empreg,leaveform
from functools import wraps
from .models import User,Post
leaveapp.secret_key = os.urandom(24)
import sqlite3
from sqlalchemy import and_,insert
from datetime import datetime

from flask_mail import Message
'''dailyupdate.config['MAIL_SERVER'] = 'smtp.gmail.com'
dailyupdate.config['MAIL_PORT'] = 465

dailyupdate.config['MAIL_USE_SSL'] = True,

dailyupdate.config['MAIL_USERNAME'] = 'lakshmiprasanna268@gmail.com'
dailyupdate.config['MAIL_PASSWORD'] = 'nana@diwakar'
dailyupdate.config['ADMINS'] = ['lakshmiprasanna268@gmail.com']'''

@dailyupdate.route('/signUp')
def signUp():
    return render_template('signUp.html')


