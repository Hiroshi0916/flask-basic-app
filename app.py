from flask import Flask, render_template
from datetime import datetime


app= Flask(__name__)

@app.template_filter('born_year')
def calcurate_corn_year(age):
    now_timestamp=datetime.now()
    return str(now_timestamp.year-int(age)) + 'year'
    

@app.template_filter('reverse_name')
def reverse(name):
    return name[-1::-1]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home/<string:user_name>/<int:age>')
def home(user_name,age):
    # login_user= user_name
    login_user={
        'name':user_name,
        'age':age
    }
    return render_template('home.html', user_info=login_user)

class UserInfo:
    def __init__(self,name,age):
        self.name=name
        self.age=age

@app.route('/userlist')
def user_list():
    # users=[
    #     'Taro','Jiro','Saburo','Shiro','Hanako'
    # ]
    users=[
        UserInfo('Taro',21), UserInfo('Jiro',32), UserInfo('Hanako',22)
    ]
    is_login=False
    return render_template('userlist.html', users=users, is_login=is_login)

    
    # return render_template('userlist.html', users=users)

if __name__ == '__main__':
    app.run(debug = True)