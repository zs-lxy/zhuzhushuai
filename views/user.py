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
    # 如果没有登录...(跳转到首页)
    if not user_mobile:
        return render_template('index/index.html')
    else:
        return render_template('index/homepage.html', user=user)


@user_blu.route("/user/user_base_info")
def user_base_info():
    # 个人主页信息展示
    user_mobile = session.get('mobile')
    # 查询user
    user = db.session.query(User).filter(User.mobile == user_mobile).first()

    # 显示个人信息(个人主页的  主页)
    return render_template("index/user_base_info.html", user=user)


@user_blu.route("/user/my_order")
def my_order():
    # 我的订单
    return render_template("index/my_order.html")


@user_blu.route("/user/my_evaluate")
def my_evaluate():
    # 我的评价
    return render_template("index/my_evaluate.html")


@user_blu.route("/user/coupon")
def coupon():
    # 我的优惠卷
    return render_template("index/coupon.html")


@user_blu.route("/user/pick_up")
def pick_up():
    # 点卷充值
    return render_template("index/pick_up.html")


@user_blu.route("/user/cash")
def cash():
    # 点卷充值
    return render_template("index/cash.html")




@user_blu.route("/user/alter_user_info")
def alter_user_info():
    # 修改个人信息
    return render_template("index/alter_user_info.html")


@user_blu.route("/user/alter_password")
def alter_password():
    # 修改密码
    return render_template("index/alter_password.html")


@user_blu.route("/user/addrs")
def addrs():
    # 收货地址
    return render_template("index/addrs.html")


@user_blu.route("/user/leave_maessage")
def leave_maessage():
    # 我的留言
    return render_template("index/leave_maessage.html")


@user_blu.route("/user/my_collect")
def my_collect():
    # 我的收藏
    return render_template("index/my_collect.html")


