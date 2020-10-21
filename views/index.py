from flask import render_template

from models import db
from models.index import Product, Category
from . import index_blu


@index_blu.route("/")
def index():
    # 查询12个男生服装
    man_dress = db.session.query(Product).filter(Product.one_category_id == 100).order_by(-Product.dress_date).limit(12)
    # 查询12个女生服装
    woman_dress = db.session.query(Product).filter(Product.one_category_id == 200).order_by(-Product.dress_date).limit(
        12)

    return render_template('index/index.html', man_dress=man_dress, woman_dress=woman_dress)
