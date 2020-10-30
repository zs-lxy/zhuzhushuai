from . import db
from datetime import datetime


class Product(db.Model):  # 货号表
    """服装"""
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)  # 货品编号
    dress_code = db.Column(db.Integer, nullable=False)  # 服装版型
    dress_brand = db.Column(db.String(256), nullable=False)  # 品牌名
    dress_info = db.Column(db.String(512), nullable=False)  # 服装信息
    dress_price = db.Column(db.String(64), nullable=False)  # 单价
    dress_img_url = db.Column(db.String(256), nullable=False)  # 产品图片/显示在首页的
    dress_date = db.Column(db.DateTime, default=datetime.now)  # 出厂日期
    dress_status = db.Column(db.String(256), nullable=False)  # 服装状态(是否有货)
    one_category_id = db.Column(db.Integer, default=200)  # 一级分类
    two_category_id = db.Column(db.Integer, nullable=False)  # 二级分类


class Color(db.Model):
    '''颜色'''
    # 根据服装版型  确定款式， 这个款式都有什么颜色
    __tablename__ = "color"

    id = db.Column(db.Integer, primary_key=True)  # id/
    code = db.Column(db.Integer, nullable=False)  # 服装版型
    yanse = db.Column(db.String(256), nullable=False)  # 衣服颜色
    s = db.Column(db.String(256), nullable=False)  # 服装尺寸 m号
    m = db.Column(db.String(256), nullable=False)  # 服装尺寸 m号
    x = db.Column(db.String(256), nullable=False)  # 服装尺寸 m号
    xl = db.Column(db.String(256), nullable=False)  # 服装尺寸 m号
    xxl = db.Column(db.String(256), nullable=False)  # 服装尺寸 m号


class Category(db.Model):
    """服装分类"""
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)  # 分类编号
    one_category_id = db.Column(db.Integer, default=200)  # 男女分类
    grop_name = db.Column(db.String(64), nullable=False)  # 分类名
    type_name = db.Column(db.String(64), nullable=False)  # 类型名
    two_category_id = db.Column(db.Integer, default=False)  # 服装类型分类


class User(db.Model):
    '''客户'''

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)  # 客户编号
    name = db.Column(db.String(32), nullable=True)  # 客户真名
    nick_name = db.Column(db.String(32), nullable=False)  # 客户昵称
    password_hash = db.Column(db.String(128), nullable=False)  # 加密的密码
    mobile = db.Column(db.String(11), nullable=False)  # 手机号
    avatar_url = db.Column(db.String(256), nullable=True)  # 用户头像路径
    create_time = db.Column(db.DateTime, default=datetime.now)  # 注册时间
    last_login = db.Column(db.DateTime, default=datetime.now)  # 最后一次登录时间
    is_admin = db.Column(db.Boolean, default=0)
    signature = db.Column(db.String(512), nullable=True)  # 用户签名
    postal = db.Column(db.Integer, nullable=True)  # 邮编
    address = db.Column(db.String(512), nullable=True)  # 省市区地址
    address_info = db.Column(db.String(512), nullable=True)  # 详细地址
    email = db.Column(db.String(512), nullable=True)  # 邮箱


class User_message(db.Model):
    '''客户留言'''

    __tablename__ = 'user_message'

    id = db.Column(db.Integer, primary_key=True)  # id
    user_grade = db.Column(db.Integer, default=1)  # 留言等级
    user_mobile = db.Column(db.String(11), nullable=True)  # 客户的电话
    user_title = db.Column(db.String(100), nullable=True)  # 留言的标题
    user_files_url = db.Column(db.String(100), nullable=True)  # 留言的标题
    user_message = db.Column(db.String(512), nullable=True)  # 留言内容


class Flow(db.Model):
    '''购物车'''

    __tablename__ = 'flow'

    id = db.Column(db.Integer, primary_key=True)  # id
    uid = db.Column(db.Integer)  # user 的id
    goods_id = db.Column(db.Integer)  # 商品 的id
    num = db.Column(db.Integer, default=1)  # 数量
    color = db.Column(db.String(11), nullable=True)  # 颜色
    size = db.Column(db.String(11), nullable=True)  # 尺码
    prices = db.Column(db.String(64), nullable=False)  # 一次的总价
    create_time = db.Column(db.DateTime, default=datetime.now)  # 创建时间
    update_time = db.Column(db.DateTime, default=datetime.now)  # 更新时间
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"))  # 商品id
    product = db.relationship("Product", backref="flow")  #和商品表关联








