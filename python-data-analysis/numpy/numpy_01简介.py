#encoding utf-8
import numpy as np

def main():
    # 01 numpy.array
    lst = [[1,2,3],[4,5,6]] #list中元素可以有多种类型
    print(type(lst))
    nplst = np.array(lst)   #nuppy.array中元素只能有一种数据类型
    print(type(nplst))
    nplst = np.array(lst,dtype=np.float)
    print(type(nplst))      #变量类型 numpy.ndarray
    print(nplst.shape)      #数组形状(2, 3)
    print(nplst.ndim)       #数据维度 2
    print(nplst.dtype)      #元素类型 float
    print(nplst.itemsize)   #元素所占字节，64位=8字节
    print(nplst.size)       #数组大小，元素个数

    # 02 numpy数组常用方法
    print(np.zeros([2,3]))
    print(np.ones([2, 3]))
    print("rand:[0,1)内均匀分布的随机数")
    print(np.random.rand(2,3))
    print(np.random.rand())
    print("randint:[1,10)内均匀分布的整型随机数")
    print(np.random.randint(1, 10))         #指定范围
    print(np.random.randint(1, 10, 2))      #指定范围+个数
    print(np.random.randint(1, 10, (2,3)))  #指定范围+尺寸
    print("randn:正态分布随机数")
    print(np.random.randn(2, 3))
    print("Choice:在指定值内随机选择")
    print(np.random.choice([1,2,10,100,33,4],[2,3]))
    print("其他数学分布随机数:beta分布")
    print(np.random.beta(1,10,100))          #[1,10]内100个满足beta分布的随机数

    #03 numpy常用操作
    #产生等差数列（数组）
    arr1 = np.arange(1,21,2); #[1,21)间隔为2：1，3，5，7，19
    #数组变形
    arr2 = np.arange(1,21,2).reshape([2,5]);
    arr2 = np.arange(1,21,2).reshape([2,-1]); #-1表示列缺省，与[2,5]等效。
    #常用数学函数
    np.sqrt(2);    #开方
    np.square(2);  #平方
    np.exp(1);     #e的指数幂
    np.exp2(3);    #2的指数幂
    np.log(np.e);  #自然对数，以e为底
    np.log2(2);    #以2为底的对数
    np.sin(1);     # sin(1)
    np.cos(1);     # cos(1)
    np.sin(1)**2 + np.cos(1)**2; # 1

    #sum 求和，默认求总和，可以指定维度。
    arr1 = np.arange(24).reshape(2, 3, 4);
    print(arr1.sum(axis=0)) #对第0维求和
    print(arr1.sum(0))
    print(np.sum(arr1,axis=0))
    print(np.sum(arr1,0))
    print(arr1.sum(axis=1)) #对第1维求和
    print(arr1.sum(axis=2)) #对第2维求和
    #max
    print(np.max(arr1))
    print(np.max(arr1, 0))
    #min
    print(np.min(arr1))
    print(np.min(arr1, 0))

    #矩阵加减乘除
    print(arr1 + arr2)
    print(arr1 - arr2)
    print(arr1 * arr2)
    print(arr1 / arr2)

    #矩阵点乘
    arr1 = np.arange(12).reshape(3, 4)
    arr2 = np.arange(12).reshape(4, 3)
    np.dot(arr1, arr2)

    #矩阵合并、追加、拆分
    arr3 = np.arange(24).reshape(2,3,4)
    np.vstack((arr3, arr3))                 #(2,3,4) ==> (4,3,4) 追加行数
    np.concatenate((arr3, arr3), axis=0)    #(2,3,4) ==> (4,3,4) 追加行数
    np.hstack((arr3, arr3))                 #(2,3,4) ==> (2,6,4) 追加列数
    np.concatenate((arr3, arr3), axis=1)    #(2,3,4) ==> (2,6,4) 追加列数




if __name__ == '__main__':
    main()