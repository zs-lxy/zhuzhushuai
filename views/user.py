from flask import jsonify, render_template, session

from models import db
from models.index import User
from views import user_blu


@user_blu.route("/user/homepage")
def homepage():
    # 个人主页
    # 查看有没有session
    user_mobile = session.get('mobile')
    # print("user_mobile",user_mobile)
    # 查询user
    user = db.session.query(User).filter(User.mobile == user_mobile).first()
    # print(user.mobile)
    # 如果没有登录...
    if not user_mobile:
        return render_template('index/homepage.html')
    else:
        return render_template('index/homepage.html', user=user)


@user_blu.route("/user/user_base_info")
def user_base_info():
    # 显示个人信息(个人主页的  主页)
    return render_template("index/user_base_info.html")



@user_blu.route("/user/my_order")
def my_order():
    # 显示个人信息(个人主页的  主页)
    return render_template("index/my_order.html")
