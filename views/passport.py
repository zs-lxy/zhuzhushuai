from flask import jsonify, request, session, url_for, redirect, make_response

from werkzeug.security import generate_password_hash, check_password_hash
from models import db
from models.index import User

from . import passport_blu


# 这里存放用passport_blu蓝图装饰的视图函数


@passport_blu.route("/passport/login_btn", methods=["GET", "POST"])
def login_btn():
    # 登录表单的
    username = request.json.get('username')
    passwd = request.json.get('passwd')
    # print("________++++++++++++___________")
    # print(username, passwd)

    # 2. 查询，如果存在表示登录成功，否则失败
    user = db.session.query(User).filter(User.mobile == username).first()
    # 判断密码和用户名  ,  如果存在
    if user and user.password_hash == passwd:
        ret = {
            'errno': 0,
            'errmsg': "登录成功.....!"
        }
        session['mobile'] = user.mobile
        session['nick_name'] = user.nick_name
        session['passwd'] = user.password_hash
    else:
        ret = {
            'errno': 800,
            'errmsg': "登录失败.....!"

        }

    return jsonify(ret)


@passport_blu.route("/passport/register_btn", methods=["GET", "POST"])
def register_btn():
    # 注册表单的
    mobile = request.json.get('mobile')
    nick_name = request.json.get('nick_name')
    password = request.json.get('password')
    confirm_password = request.json.get('confirm_password')
    image_code = request.json.get('captcha')
    agreement = request.json.get('agreement')
    print("mobile=", mobile, password, confirm_password, agreement)

    # 验证图片验证码是否争取
    print("session的",session.get("image_code"))
    print("获取的",image_code)
    if str(session.get("image_code")).upper() != str(image_code).upper():
        ret = {
            "errno": 1003,
            "errmsg": "重新输入验证码"
        }
        return jsonify(ret)

    # 查看用户是否存在
    if db.session.query(User).filter(User.mobile == mobile).first():
        ret = {
            'errno': 901,
            'errmsg': "已经注册.....!"
        }
        return jsonify(ret)

    # 将新用户的数据插入到数据库
    user = User()
    user.mobile = mobile
    user.nick_name = nick_name
    user.password_hash = password
    # hash加密
    # user.password_hash = generate_password_hash(passwd)

    try:
        db.session.add(user)
        db.session.commit()

        # 注册成功之后，立刻认为登录成功，也就说需要进行状态保持
        session['mobile'] = user.mobile
        session['nick_name'] = user.nick_name
        session['password'] = user.password_hash

        ret = {
            "errno": 0,
            "errmsg": "注册成功..."
        }
    except:
        db.session.rollback()  # 如果在将用户的信息 保存
        ret = {
            "errno": 900,
            "errmsg": "注册失败..."
        }

    return jsonify(ret)


@passport_blu.route("/passport/log_out")
def log_out():
    # 清空登录状态
    session.clear()

    return redirect(url_for('index_blu.index'))


@passport_blu.route("/passport/image_code")
def image_code():
    # 真正的生成一张图片数据
    from utlis.captcha.captcha import captcha

    # 生成验证码
    # hash值  验证码值  图片内容
    name, text, image = captcha.generate_captcha()

    print("刚刚生成的验证码：", text)
    # 通过session的方式，缓存刚刚生成的验证码，否则注册时不知道刚刚生成的是多少
    session['image_code'] = text
    # 返回响应内容
    resp = make_response(image)

    # 设置内容类型
    resp.headers['Content-Type'] = 'image/png'

    return resp
