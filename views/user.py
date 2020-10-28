import hashlib
import os
import time

from flask import jsonify, render_template, session, request

from models import db
from models.index import User, User_message
from utlis.image_qiniu import upload_image_to_qiniu
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
    # 修改个人信息   --------   已经去繁从简  只上传头像 (修改地址完成了大部分功能)
    # 个人主页信息展示
    user_mobile = session.get('mobile')
    # 查询user
    user = db.session.query(User).filter(User.mobile == user_mobile).first()

    return render_template("index/alter_user_info.html", user=user)


@user_blu.route("/user/user_avatar", methods=["POST"])
def user_avatar():
    f = request.files.get("avatar")

    if f:
        # print(f.filename)
        # 为了防止多个用户上传的图片名字相同，需要将用户的图片计算出一个随机的用户名，防止冲突
        file_hash = hashlib.md5()
        file_hash.update((f.filename + time.ctime()).encode("utf-8"))
        file_name = file_hash.hexdigest() + f.filename[f.filename.rfind("."):]

        avatar_url = file_name

        # 将路径改为static/upload下
        path_file_name = "./static/upload/" + file_name

        # 用新的随机的名字当做图片的名字
        f.save(path_file_name)

        # 将这个图片上传到七牛云
        qiniu_avatar_url = upload_image_to_qiniu(path_file_name, file_name)

        # 修改数据库中用户的头像链接（注意，图片时不放在数据库中的，数据库中存放的图片的名字或者路径加图片名）
        user_mobile = session.get("mobile")
        user = db.session.query(User).filter(User.mobile == user_mobile).first()
        user.avatar_url = qiniu_avatar_url
        db.session.commit()

        ret = {
            "errno": 0,
            "avatar_url": user.avatar_url
        }
    else:
        ret = {
            "errno": 904,
            "errmsg": "上传失败"
        }

    return jsonify(ret)


@user_blu.route("/user/alter_password")
def alter_password():
    # 修改密码
    return render_template("index/alter_password.html")


@user_blu.route("/user/alter_password_ooo", methods=["POST", "GET"])
def alter_password_ooo():
    old_p = request.json.get('oldpassword')
    new_p = request.json.get('newpassword')

    # 查询登录的用户是谁
    user_mobile = session.get('mobile')
    # 查询user
    user = db.session.query(User).filter(User.mobile == user_mobile).first()

    if user.password_hash == old_p:
        user.password_hash = new_p
    try:

        db.session.commit()
        ret = {

            'errno': 0,
            'errmsg': "修改密码成功"

        }

    except:
        db.session.rollback()  # 如果在将用户的信息 保存
        ret = {
            "errno": 903,
            "errmsg": "修改密码失败啦..."
        }
    return jsonify(ret)


@user_blu.route("/user/addrs")
def addrs():
    # 收货地址
    return render_template("index/addrs.html")


@user_blu.route("/user/addrs_oooo", methods=["POST", "GET"])
def addrs_oooo():
    input_realname = request.json.get('input_realname')
    addrs_ssq = request.json.get('addrs_ssq')
    input_address = request.json.get('input_address')
    input_postcode = request.json.get('input_postcode')
    input_mobile = request.json.get('input_mobile')
    input_email = request.json.get('input_email')

    # 查询登录的用户是谁
    user_mobile = session.get('mobile')
    # 查询user
    user = db.session.query(User).filter(User.mobile == user_mobile).first()
    user.nick_name = input_realname  # 收货人
    user.address = addrs_ssq  # 收货地址
    user.address_info = input_address  # 详细地址
    user.postal = input_postcode  # 邮编
    user.mobile = input_mobile  # 手机号
    user.email = input_email  # 邮箱

    try:

        db.session.commit()
        ret = {

            'errno': 0,
            'errmsg': "收货信息保存ok"

        }
        # 修改过程中  改变了存入session 里面的用户登录的重要信息 : 电话号
        # 把新的保存起来
        session["mobile"] = user.mobile
    except:
        db.session.rollback()  # 如果在将用户的信息 保存
        ret = {
            "errno": 902,
            "errmsg": "收货信息保存失败啦..."
        }
    return jsonify(ret)


@user_blu.route("/user/leave_message")
def leave_message():
    # 我的留言
    return render_template("index/leave_message.html")


@user_blu.route("/user/leave_message_ooo", methods=["POST"])
def leave_message_ooo():
    user_mobile = session.get("mobile")

    # 拿到form表单提交的数据  https://www.cnblogs.com/zhou--fei/p/7678025.html
    form_date = request.form.to_dict()
    # request_dict = eval(form_date.keys()[0])
    msg_type = form_date.get('msg_type')
    msg_title = form_date.get('msg_title')
    msg_content = form_date.get('msg_content')
    f = request.files.get("message_img")
    try:
        if f:
            # print(f.filename)
            # 为了防止多个用户上传的图片名字相同，需要将用户的图片计算出一个随机的用户名，防止冲突
            file_hash = hashlib.md5()
            file_hash.update((f.filename + time.ctime()).encode("utf-8"))
            file_name = file_hash.hexdigest() + f.filename[f.filename.rfind("."):]

            # 将路径改为static/upload下
            path_file_name = "./static/image/" + file_name

            # 用新的随机的名字当做图片的名字
            f.save(path_file_name)

            # 将这个图片上传到七牛云
            qiniu_avatar_url = upload_image_to_qiniu(path_file_name, file_name)

            # 修改数据库中用户的头像链接（注意，图片时不放在数据库中的，数据库中存放的图片的名字或者路径加图片名）
            user_mes = User_message()
            user_mes.user_files_url = qiniu_avatar_url
            user_mes.user_grade = msg_type
            user_mes.user_mobile = user_mobile
            user_mes.user_title = msg_title
            user_mes.user_message = msg_content
            db.session.add(user_mes)
            db.session.commit()
            ret = {
                "errno": 0,
                "errmsg": user_mes.user_files_url
            }
        # 如果没有上传图片，也可以保存留言信息
        else:
            user_mes = User_message()
            user_mes.user_grade = msg_type
            user_mes.user_mobile = user_mobile
            user_mes.user_title = msg_title
            user_mes.user_message = msg_content
            db.session.add(user_mes)
            db.session.commit()

            ret = {
                "errno": 0,
                "errmsg": 'ok'
            }
            return jsonify(ret)
    except:
        ret = {
            "errno": 905,
            "errmsg": '留言上传失败'
        }
    return jsonify(ret)


@user_blu.route("/user/my_collect")
def my_collect():
    # 我的收藏
    return render_template("index/my_collect.html")
