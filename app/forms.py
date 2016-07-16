from flask_wtf import Form

from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
from lapp.models import User,Post

class LoginForm(Form):
    username = StringField('username', validators=[DataRequired('username is invalid')])
    password = BooleanField('password', validators=[DataRequired('Password is invalid')])
    remember_me=BooleanField('remember_me',default=False)
    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        user = User.query.filter_by(
            username=self.username.data).first()
        print "user from database"
       # print user.firstname,user.password
  
        if user.firstname is None:
            self.username.errors.append('Please enter valid Username')
            return False
        if self.password.data != user.password :
            self.password.errors.append('Please enter correct Password or request HR for new password')
            return False
        self.user = user
        return user
    
