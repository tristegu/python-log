# 类的三大基本特征：封装、继承和多态
class Geese:
    neck = "脖子较长"
    wing = "振翅频率高"
    leg = "腿位于身体的中心支点，行走自如"
    beak = "喙的基部较高，长度和头部的长度几乎相等"
    __neck_swan = "天鹅的脖子很长"
    num = 0

    def __init__(self):
        Geese.num = Geese.num + 1
        print("\n我是第" + str(Geese.num) + "只大雁，我属于雁类！我有以下特征:")
        print(Geese.neck)
        print(Geese.wing)
        print(Geese.leg)
# goose1 = Geese()
# goose2 = Geese()
# goose1.neck = "我是倪博洋"
# print(goose1.neck)
# print("加入类名：", goose1._Geese__neck_swan)
# print("直接访问：", goose1.__neck_swan)


'''list_Geese = []
for i in range(4):
    list_Geese.append(Geese())
print("一共有" + str(Geese.num) + "只大雁！")
print("第2只大雁的喙：" + list_Geese[1].beak)'''

'''class Geese:
    def __init__(self):
        self.neck = "脖子较长"
        self.wing = "振翅频率高"
        self.leg = "腿位于身体的中心支点，行走自如"
        print("我属于雁类！我有以下的特征：")
        print(self.neck)
        print(self.wing)
        print(self.leg)
geese = Geese()'''


class TVshow:

    list_show = ['红海行动', '战狼2', '西游记女儿国', '熊出没-变形记']

    def __init__(self, show):
        self.__show = show

    @property  # 将方法转换成属性
    def show(self):
        return self.__show

    @show.setter   # 设置setter方法，让属性可修改
    def show(self, value):
        if value in TVshow.list_show:
            self.__show = "您选择了《" + value + "》,稍后将播放"
        else:
            self.__show = "您点播的电影不存在"


tvshow = TVshow("战狼2")
print("正在播放的是：《", tvshow.show, "》")
print("您可以从", tvshow.list_show, "中选择电影进行点播")
tvshow.show = "熊出没"
print(tvshow.show)

# 继承
'''class Fruit:      # 基类
    color = "绿色"
    def harvest(self, color):
        print("水果是：" + color + "的！")
        print("水果已经收获了！")
        print("水果原来是：" + Fruit.color + "的！")
class Apple(Fruit):              # 派生类
    # Apple(Fruit)表示Apple这个类继承了Fruit这个类的属性
    color = "红色"
    print("\n我是苹果！")
class Orange(Fruit):
    color = "橙色"
    def __init__(self):
        print("\n我是橙子!")
    def harvest(self, color):
        print("橙子是：" + color + "的！")
        print("橙子已经收获了！")
        print("橙子原来是：" + Fruit.color + "的！")

apple = Apple()
apple.harvest(apple.color)
orange = Orange()
orange.harvest(orange.color)
# 在Orange这个派生类中重写了harvest()这个函数，这边会执行改重写的函数而不是基类中的函数'''


class Fruit:
    def __init__(self, color="绿色"):
        Fruit.color = color

    def harvest(self):
        print("水果已经收获了！")
        print("水果原来是" + Fruit.color + "的！")


class Apple(Fruit):
    def __init__(self):
        print("\n我是苹果!")
        super().__init__()


class Sapodilla(Fruit):
    def __init__(self, color):
        print("\n我是人参果!")
        super().__init__(color)

    def harvest(self, color):
        print("人参果是：" + color + "的！")
        print("人参果已经收获")
        print("人参果原来是" + Fruit.color + "的！")


apple = Apple()
apple.harvest()
sapodilla = Sapodilla("白色")
sapodilla.harvest("金黄色")

