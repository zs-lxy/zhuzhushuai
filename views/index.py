from flask import render_template, redirect, url_for, session, request, jsonify

from models import db
from models.index import Product, Category, Color, User, Flow
from . import index_blu


@index_blu.route("/index")
def index_zhuye():
    return redirect(url_for('index_blu.index'))


@index_blu.route("/")
def index():
    # 看看session里面有没有用户,判断是否登录
    user = session.get('nick_name')
    print(user)

    # 查询12个男生服装
    man_dress = db.session.query(Product).filter(Product.one_category_id == 100).order_by(
        -Product.dress_date).limit(12)
    # 查询12个女生服装
    woman_dress = db.session.query(Product).filter(Product.one_category_id == 200).order_by(
        -Product.dress_date).limit(
        12)

    if user:
        return render_template('index/index.html', man_dress=man_dress, woman_dress=woman_dress, user=user)
    else:
        return render_template('index/index.html', man_dress=man_dress, woman_dress=woman_dress)


@index_blu.route("/index/goods/<int:goods_id>")
def goods(goods_id):
    # 看看session里面有没有用户,判断是否登录
    user = session.get('nick_name')

    # 拿到了商品的dress_code  查衣服
    dress = db.session.query(Product).filter(Product.dress_code == goods_id).first()

    # 查询颜色
    colors = db.session.query(Color).filter(Color.code == goods_id).all()

    return render_template('index/goods.html', user=user, dress=dress, colors=colors)


@index_blu.route('/index/goods_info', methods=["POST"])
def goods_info():
    # 拿到颜色和尺码
    tes1 = request.json.get('tes1')
    tes2 = request.json.get('tes2')
    num = request.json.get('num')
    g_code = request.json.get('g_code')  # 衣服code
    user_mobile = session.get("mobile")  # 手机号
    # 根据手机号 查询user对象
    user = db.session.query(User).filter(User.mobile == user_mobile).first()
    if user:
        # 创建购物车对象
        flow = Flow()
        flow.uid = user.id
        flow.num = num
        flow.goods_id = g_code
        flow.color = tes1
        flow.size = tes2
        print("flow.uid:", flow.uid, "num:", num, "g_code:", g_code)
        print("color:", tes1, "size:", tes2)

        try:
            # 将物品添加进购物车
            db.session.add(flow)
            db.session.commit()

            ret = {
                'errno': 0,
                'errmsg': "添加成功.....!"

            }
        except:
            db.session.rollback()
            ret = {
                'errno': 906,
                'errmsg': "添加失败.....!"

            }
        return jsonify(ret)
    else:
        ret = {
            'errno': 907,
            'errmsg': "没有登录.....!"

        }
        return jsonify(ret)


@index_blu.route('/index/flow')
def flow():
    # 判断没登录的话 跳转首页
    user_mobile = session.get("mobile")
    user = db.session.query(User).filter(User.mobile == user_mobile).first()

    # 根据id 查看购物车
    goods = db.session.query(Flow).filter(Flow.uid == user.id).first()

    if user:
        return render_template('index/flow.html', user=user, goods=goods)
    else:
        return render_template('/')
