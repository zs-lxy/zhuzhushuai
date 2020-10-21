from . import db
from datetime import datetime

class Product(db.Model):  # 货号表
    """服装"""
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)  # 货品编号
    dress_code = db.Column(db.Integer, nullable=False)  # 服装条码
    dress_brand = db.Column(db.String(256), nullable=False)  # 品牌名
    dress_color = db.Column(db.String(256), nullable=False)  # 服装颜色
    dress_size = db.Column(db.String(256), nullable=False)  # 服装尺寸
    dress_info = db.Column(db.String(512), nullable=False)  # 服装信息
    dress_price = db.Column(db.String(64), nullable=False)  # 单价
    dress_img_url = db.Column(db.String(256), nullable=False)  # 产品图片/显示在首页的
    dress_date = db.Column(db.DateTime, default=datetime.now)  # 出厂日期
    dress_status = db.Column(db.String(256), nullable=False) # 服装状态(是否有货)
    one_category_id = db.Column(db.Integer, default=200)  # 一级分类
    two_category_id = g_id = db.Column(db.Integer, nullable=False)  # 二级分类



class Category(db.Model):
    """服装分类"""
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)  # 分类编号
    one_category_id = db.Column(db.Integer, default=200)  # 男女分类
    grop_name = db.Column(db.String(64), nullable=False)  # 分类名
    type_name = db.Column(db.String(64), nullable=False)  # 类型名
    two_category_id = db.Column(db.Integer, default=False)  # 服装类型分类
