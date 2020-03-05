#encoding utf-8
import numpy as np

def main():
    import matplotlib.pyplot as plt
    # 数据准备&画图
    x = np.linspace(-np.pi, np.pi, 200, endpoint=True)
    cos1, sin1 = np.cos(x), np.sin(x)
    plt.figure(1)   # creates a new figure
    plt.plot(x, cos1, color="blue", linewidth=1.0, linestyle="-", label="cos(x)", alpha=0.5)
    plt.plot(x, sin1, "r*", label="sin(x)") #红色，*型线
    plt.title("cos(x) & sin(x)")
    plt.axis([-1, 1, -1, 1]) # 坐标轴数值范围
    plt.legend(loc="upper left") # 图例
    plt.grid() # 网格
    # 轴的编辑器
    ax = plt.gca()
    ax.spines["top"].set_color("none") #隐藏边线
    ax.spines["right"].set_color("none")
    ax.spines["left"].set_position(("data",0)) #轴线中心定位数据域的0值
    ax.spines["bottom"].set_position(("data",0))
    # 刻度线
    ax.xaxis.set_ticks_position("bottom") #刻度线显示方位
    ax.yaxis.set_ticks_position("left")
    plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
               [r'$-\pi$',r'$-\pi/2$',r'$0$',r'$+\pi/2$',r'$+\pi$']) #在python中使用laText符号 https://www.imooc.com/qadetail/221316
    plt.yticks(np.linspace(-1,1,5,endpoint=True))
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(16) # 刻度标签字体
        label.set_bbox(dict(facecolor="white", edgecolor="None", alpha=0.2)) # 刻度标签框

    # 图像填充 plt.fill_between(x, y1, y2=0, where=none, ...)
    plt.fill_between(x, np.abs(x) < 0.5, cos1, cos1 > 0.2, color="green", alpha=0.2) # 曲线1：竖线x>-0.5或x<0.5，曲线2：cos1=cos(x)，where过滤：cos1 > 0.2
    #plt.fill_between(x, cos1, cos1 > 0.2, color="red", alpha=0.2)        # 曲线1：cos1=cos(x)，曲线2：cos1 > 0.2，范围：x，where过滤：无
    #plt.fill_between(x, cos1, where=cos1 > 0.2, color="red", alpha=0.2) # 曲线1：cos1=cos(x)，曲线2：y=0，范围：x，where过滤：cos1 > 0.2
    #plt.fill_between(x, sin1, where=((np.abs(x) < 0.5) & (np.abs(x) > 0.2)), color="red", alpha=0.2) # abs(x) ∈ (0.2,0.5)
    #plt.fill_between(x, sin1, where=((np.abs(x) > 0.5) | (np.abs(x) < 0.2)), color="red", alpha=0.2) # abs(x)>0.5，或abs(x)<0.2

    # 自定义图注
    plt.plot([1,1],[0,np.cos(1)],"y",linewidth=3.0, linestyle="--", label = "cos(1)")
    plt.annotate("cos(1)", xy=(1,np.cos(1)), xycoords="data",
                 xytext = (+30,+40), textcoords="offset points", # textcoords表明xytext是一个相对(1,cos(1))的xy偏移量，不是坐标.
                 arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=0.2") # 用-->箭头连接,弧度0.2。连接线示例：https://blog.csdn.net/u013457382/article/details/50956459
                 )

    plt.savefig("./fig/matplot-fig-01.png")
    plt.show()

if __name__ == '__main__':
    main()