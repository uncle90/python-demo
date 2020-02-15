#encoding utf-8
import numpy as np

def main():
    import matplotlib.pyplot as plt

    # 新建画布
    # fig = plt.figure(figsize=[6.4,4.8])
    fig = plt.figure(figsize=[20, 12])        #调大画布尺寸，避免子图间重叠

    # 01 scatter 散点图
    ax = fig.add_subplot(3, 3, 1)             #设置子图位置
    n = 128
    X = np.random.normal(0, 1, n)             #标准正态分布随机数 n 个
    Y = np.random.normal(0, 1, n)
    T = np.arctan2(Y, X)                      #散点颜色
    #plt.axes([0.025, 0.025, 0.95, 0.95])     #画布显示范围，与子图冲突
    #plt.scatter(X, Y, s=75, c=T, alpha=0.5)  #s-size, c-color
    ax.scatter(X, Y, s=75, c=T, alpha=0.5)    #绘制子图
    plt.xlim(-1.5, 1.5), plt.xticks([])       #x范围，去除刻度线
    plt.ylim(-1.5, 1.5), plt.yticks([])
    plt.axis()                                #获取/设置坐标轴
    plt.title("Scatter")
    plt.xlabel("x")
    plt.ylabel("y")


    # 02 bar 柱状图
    fig.add_subplot(3,3,2)
    n = 10
    X = np.arange(n)
    Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
    Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
    plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
    plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')
    # 从第二副子图开始，绘图可以不基于 ax，plt等效。
    # ax = fig.add_subplot(3, 3, 2)
    # ax.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
    # ax.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')
    for x, y in zip(X, Y1):
        plt.text(x+0.4, +y+0.09, '%.2f'%y, ha='center', va='top')     # 数据格式化："'%格式'%变量"
    for x, y in zip(X, Y2):
        plt.text(x+0.4, -y-0.09, '%.2f'%y, ha='center', va='bottom') # va: top-柱状图在横轴上,柱状图在横轴下
    plt.title("Bar")


    # 03 pie 饼图
    fig.add_subplot(3,3,3)
    n = 20
    Z = np.ones(n)
    Z[-1] *= 2
    plt.pie(Z, explode=Z*0.05, colors=['%f'%(i/float(n)) for i in np.arange(n)],
            labels=['%.2f'%(i/float(n)) for i in np.arange(n)])
    plt.gca().set_aspect('equal')  # 饼为正圆，非椭圆
    plt.xticks([]), plt.yticks([])
    plt.title("Pie")

    # 04 polar 极坐标
    fig.add_subplot(3,3,4,polar=True)
    n = 20
    theta = np.arange(0, 2 * np.pi, 2 * np.pi / n)
    radius = 10 * np.random.rand(n)
    #plt.plot(theta, radius)
    plt.polar(theta, radius)
    plt.title("Polar")

    # 05 热力图 heatmap
    fig.add_subplot(3,3,5)
    from matplotlib import cm # colormap
    data = np.random.rand(10,10)
    color_map = cm.Blues
    map = plt.imshow(data, interpolation='nearest', cmap=color_map, aspect='auto', vmin=0, vmax=1) # aspect 尺寸缩放
    plt.title("Heat Map")


    # 06 3D图
    from mpl_toolkits.mplot3d import  Axes3D
    ax = fig.add_subplot(3,3,6, projection="3d")
    n = 128
    X = np.random.normal(0, 1, n)  # 标准正态分布随机数 n 个
    Y = np.random.normal(0, 1, n)
    Z = np.random.normal(0, 1, n)
    ax.scatter(X,Y,Z,s=5)
    plt.title("3-D")


    # 07 hot spot map 热点图
    fig.add_subplot(3,1,3) #3行1列第三列
    def f(x, y):
        return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)
    n = 128
    x = np.linspace(-2.5, 2.5, n)
    y = np.linspace(-2.5, 2.5, n)
    X, Y = np.meshgrid(x, y)
    plt.contourf(X, Y, f(X,Y), 20 , alpha=0.5, cmap = plt.cm.hot)
    plt.title("Hot Spot Map")

    plt.savefig("./fig/matplot-fig-02-多子图合并.png")
    plt.show()


if __name__ == '__main__':
    main()