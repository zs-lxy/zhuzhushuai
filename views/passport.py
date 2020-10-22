from flask import jsonify, request

from . import passport_blu


# 这里存放用passport_blu蓝图装饰的视图函数


@passport_blu.route("/passport/login_btn", methods=["GET", "POST"])
def login_btn():
    print(request.args)
    print(request.form)
    username = request.json.get('username')
    passwd = request.json.get('passwd')
    print("________++++++++++++___________")
    print(username, passwd)

    ret = {
        'errno': 0,
        'errmsg': "登录成功.....!"

    }
    return jsonify(ret)
