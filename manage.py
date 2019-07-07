# -*- encoding=UTF-8 -*-

from B2B import app, db
from flask_script import Manager
from B2B.models import User, Good, GoodType, InboundLoad, outboudLoad, warningLoad, Order, Warehouse, Image

manager = Manager(app)


@manager.command
def init_database():
    db.drop_all()
    db.create_all()

    db.session.add(GoodType('肉类', '来自西藏', '西藏的牛羊肉，可以溢价，质量特别好'))
    db.session.add(GoodType('手工礼品', '刚到货', '精美手工礼品，新颖，好玩'))
    db.session.add(GoodType('水果', '优质水果', '大部分进口'))
    db.session.add(GoodType('零食', '进口零食', '最新的零食，越南仓进口'))

    db.session.add(Good('进口红牛', 1000, '进口红牛，加气加强版', '零食', 15, 20, 23, '', '北京仓'))
    db.session.add(Good('芒果', 999, '来自泰国的进口芒果，产地甄选，用美食满足你的味蕾。', '水果', 6.00, 10.00, 15.00, '', '哈尔滨仓'))
    db.session.add(Good('火鸡面', 889, '进口山羊肉，在山上长大的山羊', '零食', 8, 10, 12, '', '北京仓'))
    db.session.add(Good('百岁山', 666, '天然矿泉水', '零食', 1, 2, 2.5, '', '北京仓'))
    db.session.add(Good('吐司', 88, '优质土司，名牌，新到货，老板的最爱', '零食', 15, 20, 23, '', '北京仓'))
    db.session.add(Good('香蕉', 88, '优质香蕉，越南仓新发货，甜到腻，放不坏', '水果', 9, 10, 13, '', '北京仓'))


    db.session.add(InboundLoad('进口红牛', '零食', 15.20, 1000, '北京仓', '2018-12-08', '好货'))
    db.session.add(InboundLoad('芒果', '水果', 6.00, 1000, '哈尔滨仓', '2018-12-08', '好货'))

    db.session.add(outboudLoad('进口红牛', '零食', 200, '北京仓', '2018-12-09', '好货'))
    db.session.add(outboudLoad('芒果', '水果', 300, '哈尔滨仓', '2018-12-08', '好货'))

    db.session.add(warningLoad('进口红牛', '零食', '北京仓', 1000, '备注'))
    db.session.add(warningLoad('芒果', '水果', '哈尔滨仓', 1000, '备注'))
    db.session.add(warningLoad('火鸡面', '零食', '北京仓', 1000, '备注'))
    db.session.add(warningLoad('吐司', '零食', '北京仓', 500, '备注'))

    db.session.add(Warehouse('北京仓', '北京市中关村22号', '该仓库很大'))
    db.session.add(Warehouse('哈尔滨仓', '哈尔滨市南岗区18号', '该仓库很小'))

    db.session.add(Image('/static/images/hongniu.png', 1, 1))
    db.session.add(Image('/static/images/hongniuc1.jpg', 1, 0))
    db.session.add(Image('/static/images/hongniuc2.jpg', 1, 0))
    db.session.add(Image('/static/images/hongniuc3.jpg', 1, 0))
    db.session.add(Image('/static/images/hongniuc4.jpg', 1, 0))
    db.session.add(Image('/static/images/hongniuc5.jpg', 1, 0))
    db.session.add(Image('/static/images/hongniuc6.jpg', 1, 0))
    db.session.add(Image('/static/images/hongniuc7.jpg', 1, 0))
    db.session.add(Image('/static/images/hongniuc8.jpg', 1, 0))

    db.session.add(Image('/static/images/mangguo.png', 2, 1))
    db.session.add(Image('/static/images/content1.jpg', 2, 0))
    db.session.add(Image('/static/images/content2.jpg', 2, 0))
    db.session.add(Image('/static/images/content3.jpg', 2, 0))
    db.session.add(Image('/static/images/content4.jpg', 2, 0))
    db.session.add(Image('/static/images/content5.jpg', 2, 0))

    db.session.add(Image('/static/images/huojimian.png', 3, 1))
    db.session.add(Image('/static/images/huojimianc1.png', 3, 0))
    db.session.add(Image('/static/images/huojimianc2.png', 3, 0))
    db.session.add(Image('/static/images/huojimianc3.png', 3, 0))
    db.session.add(Image('/static/images/huojimianc4.png', 3, 0))
    db.session.add(Image('/static/images/huojimianc5.png', 3, 0))

    db.session.add(Image('/static/images/baisuishan.png', 4, 1))
    db.session.add(Image('/static/images/baisuishanc1.png', 4, 0))
    db.session.add(Image('/static/images/baisuishanc2.png', 4, 0))
    db.session.add(Image('/static/images/baisuishanc3.png', 4, 0))

    db.session.add(Image('/static/images/tusi.png', 5, 1))
    db.session.add(Image('/static/images/tusic1.jpg', 5, 0))
    db.session.add(Image('/static/images/tusic2.jpg', 5, 0))
    db.session.add(Image('/static/images/tusic4.jpg', 5, 0))

    db.session.add(Image('/static/images/xiangjiao.png', 6, 1))
    db.session.add(Image('/static/images/xiangjiaoc1.jpg', 6, 0))
    db.session.add(Image('/static/images/xiangjiaoc2.jpg', 6, 0))
    db.session.add(Image('/static/images/xiangjiaoc3.jpg', 6, 0))
    db.session.add(Image('/static/images/xiangjiaoc4.jpg', 6, 0))
    db.session.add(Image('/static/images/xiangjiaoc5.jpg', 6, 0))
    db.session.commit()


if __name__ == '__main__':
    manager.run()