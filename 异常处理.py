import random
# print(random.randint(0, 10))

#  设置符合条件的验证码


if __name__ == '__main__':
    checkcode = ''
    for i in range(4):
        index = random.randint(0, 4)
        if index != i and index+1 != i:
            checkcode += chr(random.randint(97, 122))
        elif index + 1 == i:
            checkcode += chr(random.randint(65, 90))
        else:
            checkcode += str(random.randint(1, 9))
    print('验证码是：', checkcode)

#  分苹果（try...except.....else.....finally）
#  如果division函数没有报错，就会编译else语句
#  无论有误报错，都会编译finally语句


def division():
    print("-------------分苹果了！------------")
    apple = int(input("请输入苹果的数量："))
    children = int(input("请输入小朋友的数量："))
    if apple < children:
        raise ValueError('苹果太少了不够小朋友们分.....')
   #  assert apple > children ,"苹果太少了不够小朋友们分...."
    result = apple//children
    remain = apple - result*children
    if remain > 0:
        print(apple, "个苹果，平均分给", children, "个小朋友，每人分", result
              , "个，还剩下", remain, "个苹果")
    else:
        print(apple, "个苹果，平均分给", children, "个小朋友，每人分", result, "个!")


if __name__ =='__main__':
    try:
        division()
    except ZeroDivisionError:
        print("\n出错了——苹果不能被零个小朋友分")
    except ValueError as e:
        print('\n出错了', e)
    except AssertionError as h:
        print('\n出错了', h)
    else:
        print('分苹果成功！')
    finally:
        print('进行了一次分苹果！')