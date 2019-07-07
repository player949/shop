from B2B import db
from B2B.models import Good, warningLoad, InboundLoad
# class InboundMaker:
#     def run(self):
#         print ("自动生成进货订单")
#
# class WarningMaker:
#     def run(self):
#         print ("主页警告通知")
#
# class WareRemover:
#     def run(self):
#         print ("下架商品")


# 将三个类提取共性，泛化出“观察者”类，并构造被观察者。
class Observer:
    def update(self):
        pass


class InboundMaker(Observer):
    def update(self, action):
        print("开始生成进货订单，收到信息： %s 数量不足" % action)
        goods = action.split(' ')
        for goodname in goods:
            if(goodname != ''):
                db.session.add(InboundLoad(goodname, '零食', 999, 100, '北京仓', '2019-04-18', '好货'))
        db.session.commit()
        self.runInbounder()

    def runInbounder(self):
        print("已经生成进货订单")


class WarningMaker(Observer):
    def update(self, action):
        print("生成警告通知管理员，收到信息：%s 数量不足" % action)
        self.runWarner()

    def runWarner(self):
        print("已经通知管理员")


class WareRemover(Observer):
    def update(self, action):
        print("准备下架缺货产品，收到信息：%s 数量不足" % action)
        self.runRemover()

    def runRemover(self):
        print("开始下架商品")


# 被观察者
class Observed:
    observers = []
    action = ""

    def addObserver(self, observer):
        self.observers.append(observer)

    def notifyAll(self):
        for obs in self.observers:
            obs.update(self.action)

# 库存预警器
class InventoryWarner(Observed):
    def setAction(self, action):
        self.action = action

    def isShort(self):
        warning_list = warningLoad.query.all()
        for a in warning_list:
            # 如果预警的数量大于现有的数量，需要进货
            if int(a.quantity) > int(Good.query.filter_by(name=a.name, warehouse_name=a.warehouse_name).all()[0].quantity):
                self.action = self.action + a.name+" "
        if self.action != "":
            return True
        return False

