from app import app
from flask import render_template,request,redirect
from .forms import LoginForm

@app.route('/')
def index():
    return "<table><tr><h1>hello,world</h1></tr><tr><h2>Hello Nexii</h2></tr></table>"

@app.route('/index')
def main():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method=='POST':
        if form.validate() == False:
            return render_template('login2.html',form=form)
        else:
            return redirect('/index')
    else:  
        return render_template('login2.html',form=form)
    
