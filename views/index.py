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

    user_mobile = session.get('mobile')

    # 查询12个男生服装
    man_dress = db.session.query(Product).filter(Product.one_category_id == 100).order_by(
        -Product.dress_date).limit(12)
    # 查询12个女生服装
    woman_dress = db.session.query(Product).filter(Product.one_category_id == 200).order_by(
        -Product.dress_date).limit(
        12)
    user = db.session.query(User).filter(User.mobile == user_mobile).first()

    if user:
        # 查询该id 下单 所有物品的个数

        counts = db.session.query(Flow).filter(Flow.uid == user.id).count()
        return render_template('index/index.html', man_dress=man_dress, counts=counts, woman_dress=woman_dress,
                               user=user)
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
    # 查询商品对象
    pr = db.session.query(Product).filter(Product.dress_code == g_code).first()
    if user:
        # 创建购物车对象
        flow = Flow()
        flow.uid = user.id
        flow.num = num
        flow.goods_id = g_code
        flow.prices = float(num) * float(pr.dress_price)
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
    # 用户对象
    user = db.session.query(User).filter(User.mobile == user_mobile).first()

    # 根据id 查看购物车对象
    goods = db.session.query(Flow).filter(Flow.uid == user.id).all()
    # 查询该id 下单 所有物品的个数
    counts = db.session.query(Flow).filter(Flow.uid == user.id).count()
    # 应付金额
    yingfu = 0
    for good in goods:
        pri = float(good.prices) * float(good.num)
        yingfu += pri
        yingfu = float('%.2f' % yingfu)

    if user:
        return render_template('index/flow.html', user=user, goods=goods, counts=counts, yingfu=yingfu)
    else:
        return render_template('/')


@index_blu.route('/index/order_form')
def order_form():
    # 判断没登录的话 跳转首页
    user_mobile = session.get("mobile")
    # 用户对象
    user = db.session.query(User).filter(User.mobile == user_mobile).first()
    # 查询用户对应的购物车对象
    goods = db.session.query(Flow).filter(Flow.uid == user.id).all()
    # 应付金额
    yingfu = 0
    for good in goods:
        pri = float(good.prices) * float(good.num)
        yingfu += pri
        yingfu = float('%.2f' % yingfu)
    if user:
        return render_template('index/order_form.html', user=user, yingfu=yingfu)
    else:
        return render_template('/')


@index_blu.route('/index/order_ooo', methods=["POST"])
def order_ooo():
    # 拿到地址  (也可以数据库查询)
    name = request.json.get('name')
    mobile = request.json.get('mobile')
    addr = request.json.get('addr')
    addr_info = request.json.get('addr_info')
    zt = request.json.get('zt')
    sf = request.json.get('sf')

    user = db.session.query(User).filter(User.mobile == mobile).first()

    flow = db.session.query(Flow).filter(Flow.uid == user.id).first()
    # 库存表
    # 查到对应的颜色
    color = db.session.query(Color).filter(Color.yanse == flow.color).first()

    ret = {
        'errno': 0,
        'errmsg': "%s%s库存-1.....!" % (color.yanse, flow.size)

    }

    return jsonify(ret)
