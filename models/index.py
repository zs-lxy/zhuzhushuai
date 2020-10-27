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
    dress_status = db.Column(db.String(256), nullable=False)  # 服装状态(是否有货)
    one_category_id = db.Column(db.Integer, default=200)  # 一级分类
    two_category_id = db.Column(db.Integer, nullable=False)  # 二级分类


class Category(db.Model):
    """服装分类"""
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)  # 分类编号
    one_category_id = db.Column(db.Integer, default=200)  # 男女分类
    grop_name = db.Column(db.String(64), nullable=False)  # 分类名
    type_name = db.Column(db.String(64), nullable=False)  # 类型名
    two_category_id = db.Column(db.Integer, default=False)  # 服装类型分类


class Supplier(db.Model):
    '''供应商'''
    __tablename__ = 'supplier'

    id = db.Column(db.Integer, primary_key=True)  # id
    factory_number = db.Column(db.Integer, nullable=False)  # 厂号
    factory_name = db.Column(db.String(64), nullable=False)  # 厂名
    factory_person = db.Column(db.String(64), nullable=False)  # 联系人
    factory_phone = db.Column(db.Integer, nullable=False)  # 电话
    factory_address = db.Column(db.String(64), nullable=False)  # 地址


class Pro_Sup(db.Model):
    """中间表"""
    __tablename__ = "pro_sup"
    category_id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'), primary_key=True)


class Supply(db.Model):
    '''供应'''

    __tablename__ = 'supply'

    id = db.Column(db.Integer, primary_key=True)  # id
    dress_code = db.Column(db.Integer, nullable=False)  # 服装条码
    factory_number = db.Column(db.Integer, nullable=False)  # 厂号
    pricing = db.Column(db.Integer, nullable=False)  # 定价
    supply_num = db.Column(db.Integer, nullable=False)  # 供应数量
    supply_date = db.Column(db.DateTime, default=datetime.now)  # 供应日期


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
    '''客户'''

    __tablename__ = 'user_message'

    id = db.Column(db.Integer, primary_key=True)  # id
    user_id = db.Column(db.String(32), nullable=True)  # 客户真名
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