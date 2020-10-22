from flask import render_template, redirect, url_for, session

from models import db
from models.index import Product, Category
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
