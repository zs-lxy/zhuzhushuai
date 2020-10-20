from . import db


class Product(db.Model):  # 货号表
    """服装"""
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)  # 货品编号
    title = db.Column(db.String(256), nullable=False)  # 品牌名
    color = db.Column(db.String(256), nullable=False)  # 服装颜色
    size = db.Column(db.String(256), nullable=False)  # 服装尺寸
    content = db.Column(db.Text, nullable=False)  # 服装类型
    factory_price = db.Column(db.String(64), nullable=False)  # 出厂价
    selling_price = db.Column(db.String(64), nullable=False)  # 零售价
    digest = db.Column(db.String(512), nullable=False)  # 产品信息
    img_url = db.Column(db.String(256), nullable=False)  # 产品图片/显示在首页的

    clicks = db.Column(db.Integer, default=0)  # 出厂日期


class Category(db.Model):
    """服装分类"""
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)  # 分类编号
    g_id = db.Column(db.Integer, default=False)  # 男女分类
    grop_name = db.Column(db.String(64), nullable=False)  # 分类名
    type_name = db.Column(db.String(64), nullable=False)  # 类型名
    t_id = db.Column(db.Integer, default=False)  # 服装类型分类
