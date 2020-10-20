from flask import render_template

from models import db
from models.index import Product
from . import index_blu


@index_blu.route("/")
def index():
    # 查询最新的服装
    product = db.session.query(Product).order_by(-Product.clicks).limit(12)
    return render_template('index/index.html',product=product)

