# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#创建对象的基类
Base = declarative_base()

class User(Base):
    # 表的名字
    __tablename__ = 'user'

    # 表的结构
    id = Column(String(20), primary_key = True)
    name = Column(String(20))

# 初始化连接， '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
DBSession = sessionmaker(bind=engine) # 数据库连接

# 以上创建了ORM


# 向数据库中添加一行记录（添加一个User对象）
session = DBSession()
new_user = User(id='5', name='Bob')  # 创建一个新User对象
session.add(new_user)   # 添加到session
session.commit()  # 提交，即保存到数据库
session.close()  # 关闭session


#查询数据
session = DBSession()
user = session.query(User).filter(User.id==5).one()
print('type:', type(user))
print('name:', user.name)
session.close()  # 查完关闭连接
