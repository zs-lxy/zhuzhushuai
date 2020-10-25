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


@user_blu.route("/user/user_info")
def user_info():
    return render_template("index/user_info.html")