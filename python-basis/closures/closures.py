# 闭包1：内层函数与外层函数输入参数绑定，静态方法（闭包）返回静态结果
def make_closure(a):
    def closure():
        print('I know the secret: %d' %a)
    return closure
#测试
closure = make_closure(5) #获取闭包函数
closure() #调用



# 闭包2：内层函数输出与调用时的入参绑定，内层函数中使用了可变对象（列表、字典、集合等），返回一个能够记录曾经传入的一切参数的函数
def make_watcher():
    have_seen = {}
    def has_been_seen(x):
        if x in have_seen:
            return True
        else:
            # 使用可变对象
            have_seen[x] = True
            return False
    return has_been_seen
#测试
watcher = make_watcher() #获取闭包函数
vals = [5, 6, 1, 5, 1, 6, 3, 5]
result2 = [watcher(x1) for x1 in vals] #调用
print(result2)



#闭包3：内层函数构造与外层函数入参绑定，返回动态方法
#       内层函数输出与调用时的入参绑定，返回动态结果
#字符串格式化函数
def format_add_padding(template, space):
    def formatter(x):
        return (template % x).rjust(space)
    return formatter
#测试
fmt = format_add_padding('%.4f', 15) #格式化函数：保留4位小数，右对齐，不足15则左侧补空格
result3 = fmt(1.56)
print(result3)