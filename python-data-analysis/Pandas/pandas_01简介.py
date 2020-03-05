import numpy as np
import pandas as pd

# 01 Series
s = pd.Series([1, 3, 5, np.nan, 6, 8])
dates = pd.date_range('20130101', periods=6)
dates = pd.date_range('2013-01-01', periods=6)
dates = pd.date_range('2013/01/01', periods=6)


# 02 DataFrame
#普通创建
# 横轴=行=索引(index)，纵轴=列(column)
df = pd.DataFrame(np.random.randn(6, 4))
df = pd.DataFrame(np.random.randn(6, 4), index=dates)
df = pd.DataFrame(np.random.randn(6, 4), columns=list('ABCD'))
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

#用字典创建
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})


# 03 Pandas常用属性、方法
df.dtypes       #DataFrame每列数据的类型
df.index        #取（行）索引
df.columns      #取（列）列名
df.T            #行列转换（转置）
df.copy()       #拷贝当前DataFrame变量，修改互不影响。
df.head()       #取前n行数据，默认全部
df.tail()       #取后n行数据，默认全部
df.describe()   #对纯数字column进行数学统计
df.to_numpy()   #Pandas数组转Numpy数组。Pandas数组每列类型不一致时，to_numpy操作代价高。
df.sort_index() #按数据索引排序
# df.sort_index(axis=0,ascending=True) #按行索引升序
# df.sort_index(axis=1,ascending=True) #按列索引升序
df.sort_values(by='A')#按数据大小排序
df.sort_values(axis=0, by='A', ascending=True) #沿行方向，按列（column='A'）升序。
df.sort_values(axis=1, by='2013-01-02', ascending=True) #各列方向，按行（index='2013-01-02'）升序。


# 04 Pandas取数、切片
# (1)简化式——按列取数
df['A']
df.A
df[['A','B','C']]

# (2)简化式——按行取数
df[0:3]
df['20130102':'20130104']

# (3) 函数式——按标签取数【推荐】 i,j = index, column
# .loc   按标签取数，返回数组（行、列、切片、单个值）
# .at    按标签取数，返回单个值
df.loc[dates[0]]      # dates[0] = '2013-01-01'
df.loc['20130101']
df.loc[:, 'A']
df.loc[:, 'A':]
df.loc[:, 'A':'B']
df.loc[:, ['A', 'B']]
df.loc[dates[0:2],'B':]
df.loc[dates[0:],'B':]
df.loc['20130102':'20130104', ['A', 'B']] #行标签不支持list枚举
df.loc[dates[0],'B'] #取单个值
df.at[dates[0],'B']  #取单个值

# (4) 函数式——按位置取数【推荐】 index i,j = 0,1,2,..,n-1
# .iloc  按位置取数，返回数组（取行、列、切片、单个值）
# .iat   按位置取数，返回单个值
df.iloc[0]      # 第一行
df.iloc[:, 0]   # 第一列
df.iloc[3:5, 0:2]
df.iloc[[1, 2, 4], [0, 2]] # 行、列枚举
df.iloc[1:3, :] # 行切片
df.iloc[:, 1:3] # 列切片
df.iloc[1, 1]   #取单个值
df.iat[1, 1]    # 取单个值

# (5) 布尔索引——按条件取数（筛选）
df[df>0]        #按值筛选，不符合条件置为NaN
df[df['A'] > 0] #按行筛选，找出A列中所有大于0的行
df2 = df.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
df2[df2['E'].isin(['two', 'four'])] #按行筛选，找出E列中所有包含指定值的行


# (6) Pandas 赋值
# (a) 利用索引给某列赋值，会自动匹配Series或DataFrame变量的index，无匹配项时值为NaN！！！
df2 = df.copy();
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130101', periods=6)) #与df2的index相同
s2 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102', periods=6)) #与df2的index有交集
s3 = pd.Series([1, 2, 3, 4, 5, 6]) #与df2的index没有交集
df2['E'] = s1
df2['E'] = s2
df2['E'] = s3
# (b) 根据行、列位置赋值时，不匹配索引。
df2.at[dates[0], 'A'] = 0                 #根据标签赋值
df2.iat[0, 1] = 0                         #根据位置赋值
df2.loc[:, 'D'] = np.array([5] * len(df)) #用 numpy 数组赋值


# reindex - 增/删/改旧变量的行、列索引，返回新数据集——重构。
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df.dropna(how='any') #删除缺失值
df.fillna(value=5)   #填充缺失值
pd.isna(df)          #判断是否为缺失值，获取缺失值mask

df.mean()            #沿纵轴求均值，默认axis=0
df.mean(0)           #沿纵轴求均值，axis=0
df.mean(1)           #沿横轴求均值，axis=1
df.apply(np.sum)     #对变量运用 计算/函数/方法/匿名方法

# 平移坐标轴，数据默认不对齐
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)

#计算频率直方图/统计频次
s = pd.Series(np.random.randint(0, 7, size=10))
s.value_counts()

#数据合并 merge。DataFrame添加列容易，添加行难（会有copy操作）！！
df = pd.DataFrame(np.random.randn(10, 4))
pieces = [df[:3], df[3:7], df[7:]]
pd.concat(pieces)
#数据连接 —— SQL结果合并
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
pd.merge(left, right, on='key') #合并列
left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})
pd.merge(left, right, on='key') #合并航、列
#分组 groupby。"group by"一般包含多个步骤，数据分组 + 调用函数 + 合并结果
df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                         'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three',
                         'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})
df.groupby('A').sum()
df.groupby(['A', 'B']).sum()

#数据变形 reshape：2D <==> 1D，压缩 vs 解压。
# MultiIndex - 把元组、列表等数组转变成多级索引(Hierarchical Index)
# pd.MultiIndex.from_arrays()
# pd.MultiIndex.from_tuples()
# pd.MultiIndex.from_product()
# pd.MultiIndex.from_frame()
tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                     'foo', 'foo', 'qux', 'qux'],
                    ['one', 'two', 'one', 'two',
                     'one', 'two', 'one', 'two']])
              )
index = pd.MultiIndex.from_tuples(tuples, names=['1st', '2nd'])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
# stack 压缩 2D ==> 1D
stacked = df.stack()
# unstack 压缩 2D ==> 1D
stacked.unstack()

#数据透视表（Pivot tables）
df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 3,
                   'B': ['A', 'B', 'C'] * 4,
                   'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                   'D': np.random.randn(12),
                   'E': np.random.randn(12)}
                  )
pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])

#时间序列
rng = pd.date_range('1/1/2012', periods=100, freq='S')
rng = pd.date_range('3/6/2012', periods=100, freq='D')
rng = pd.date_range('1/1/2012', periods=100, freq='M')
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
#重采样
ts.resample('5Min').sum()
#时区转换
ts_utc = ts.tz_localize('UTC')
ts_utc.tz_convert('US/Eastern')
#切换时间表示 - 时间戳 vs 阶段
ps = ts.to_period()
ps.to_timestamp()
#按季度统计
prng = pd.period_range('1990Q1', '2000Q4', freq='Q-NOV')
ts = pd.Series(np.random.randn(len(prng)), prng)
ts.index = (prng.asfreq('M', 'e') + 1).asfreq('H', 's') + 9