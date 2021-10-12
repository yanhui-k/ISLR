# -*- coding = utf-8 -*-
# @Time : 2021/10/10 20:43
# @Author : 严慧
# @File : 第二章.py
# @Software : PyCharm

x=[1,6,2]
y=[1,4,3]
len(x)
len(y)

z={}
for i in range(3):
    z[i]=x[i]+y[i]
z

# 构建二维表
listA=[[0 for i in range(3)] for j in range(2)]
listA[1][2]=1
listA[0][1]=-1

import numpy as np
import random

nd=np.array([[1,2,3],[4,5,6]])#构建矩阵
print(nd.shape)#矩阵的维度
x0 = np.arange(1, 11, 2)
print(x0)
x1 = np.arange(15).reshape((5, 3))
print(x1)
for i in np.arange(9):#arange从0开始不含终值
    print(i)

# 创建一个 3x4 的数组且所有值全为 0
x3 = np.zeros((3, 4), dtype=int)
print(x3)
# 创建一个 3x4 的数组且所有元素值全为 1
x4 = np.ones((3, 4), dtype=int)
print(x4)
# 创建一个 3x4 的数组，然后将所有元素的值填充为 2
x5 = np.full((3, 4), 2, dtype=int)
print(x5)
# 创建 3x3 的单位矩阵,对角线值为1，其他为0
x6 = np.eye(3, dtype=int)
print(x6)
x7 = np.diag([1, 2, 3])
print(x7)
# 创建 2x2 数组且所有值是随机填充
x9 = np.random.random((2, 2))
print(x9)
# 创建一个值在 [0, 10) 区间的 3x3 的随机整数
x10 = np.random.randint(0, 10, (3, 3))
print(x10)

#数据框的输入输出
import pandas as pd
temp=pd.read_csv("Auto.csv")
temp.to_excel("auto.xlsx")
#数据框的创建
df = pd.DataFrame([[np.nan, 2, np.nan, 0],
                   [3, 4, np.nan, 1],
                   [np.nan, np.nan, np.nan, 5],
                   [np.nan, 3, np.nan, 4]],
                   columns=list('ABCD'))
#通过字典创建df
test_dict = {'A':[np.nan,3,np.nan,np.nan],
             'B':[2,4,np.nan,3],
             'C':[np.nan,np.nan,np.nan,np.nan],
             'D':[0,1,5,4]}
df2 = pd.DataFrame(test_dict)
# 查看前几行与后几行
temp.head()
temp.tail()
# 查看df行列数
temp.shape
temp.shape[1] # 单独查看列数
# 查看df各变量描述性统计
temp.describe()
temp.info()
# 查看df列名
temp.columns

### 修改部分列名
temp_1 = temp.copy()
temp_1.rename(columns={'mpg':'每秒公里数'},inplace=True)
#添加一列
temp_1['test'] = 1
#通过原有列简单计算
temp_1['test2'] = temp_1['origin'] + temp_1['test']
#基于原有列增加列
temp_1['test3'] = temp_1['test2'].apply(lambda x: '4' if x>2 else '1')
#temp_1[(int(temp_1['test3'])> 3) &(int(temp_1['test2'])== 2) ,'newtest'] = 1

def cal_label(cyl,mpg):
    if (cyl==8) & (mpg>25):
        return 'High'
    elif (cyl==4) | (mpg<15):
        return 'Low'
    else:
        return 'Medium'

temp_1['test4'] = temp_1.apply(lambda x: cal_label(x['cylinders'],x['每秒公里数']),axis=1)
#去掉
temp_1.drop(1,axis=0).head()
temp.drop("test4",axis=1).head()
#真正删除
del temp["test4"]
## 选取第2-4行
temp[2:5]
#从0开始数，2-4行
## iloc用法：通过行数筛选，eg：选择第4行
temp.iloc[3]

## 选择行index为9的行
temp.loc[9]

## 筛选出mpg列<=10的所有行
temp[temp["mpg"]<=10]
list(temp["name"][temp["mpg"]<=10])#列出mpg小于10的所有行的name

#列切片
temp_1[["mpg","cylinders"]]
temp.iloc[:,1:3]#不包括终止值
temp.iloc[2:5,1:3]#均不包括终止值
temp.iloc[[1,2,4],[1,3]]
## 用冒号表示所有行/所有列
temp.iloc[1:3,:]
temp.iloc[:,1:3]
## 选择某个值
temp.iloc[0,0]
## 条件筛选
temp[temp['cylinders']==8]
temp[temp['cylinders'].isin([4,6])] # isin是用list筛选
temp[~(temp['cylinders'].isin([4,6]))] #~是非
# 排序：sort
temp = temp.sort_values(by=['mpg','displacement']).head() # 升序
temp = temp.sort_values(by=['mpg'],ascending=False).head() # 降序
# 去重：drop_duplicates
temp_1["mpg"].unique()

## 按某列值去重
temp.drop_duplicates(subset=['mpg']).head() #可以添加keep = first类似的参数

## 去重同时保留最大值
temp = temp_1.sort_values(by=['mpg','displacement'])
temp.drop_duplicates(subset=['mpg'],keep='last').head()

# 空值：dropna/fillna
# 每一列有几个空值
df2.isnull().sum()

#删除缺失值记录
# 删除A,B列都是缺失值的行
df2.dropna(subset=['A','B'], how='all')

#填补缺失值
# 用0填补缺失值
df2.fillna(0)

# 用指定值填充/替换
values ={'A':0,'B':1,'C':2}
df2.fillna(value=values)

df2['A'].replace(np.nan,'A',inplace=True)
df2.head()

# 宽表转长表，长表转宽表
## 长转宽：
temp_pivot = pd.pivot_table(temp, values='displacement', # 列变行之后的值
                           index=['mpg'], # 保留的列值
                           columns=['cylinders'], # 列变行之后，列名
                           aggfunc=np.sum).reset_index()
### 长转宽之后转换行名为单一维度
temp_pivot.columns = ["".join((j)) for i,j in temp_pivot.columns]

## 宽转长：
temp_melt = pd.melt(temp_pivot,
                    id_vars=['mpg'],# 保留的列值
                    value_vars=[3,4,5,6,8],# 转换为列值
                    var_name='cylinders',# 列名
                    value_name='value')

# 统计值
temp.loc["max"] = temp.max(axis=0)

## 针对离散型变量对每个值计数
temp['cylinders'].value_counts()

## 统计每个值占比
temp['cylinders'].value_counts(normalize=True)

## 非重复值计数
temp['cylinders'].nunique()

## 对数值型变量进行基本的描述性统计
temp['mpg'].describe()

# group by
temp_groupby = temp.groupby(['cylinders','origin'])['weight'].mean().reset_index().sort_values(by=['weight'])

temp['排名'] = temp.groupby(['cylinders','origin'])['weight'].rank(ascending=0, method='min')
temp[temp["排名"]>100]

# 分组排名
temp = temp.groupby(['cylinders','origin']).sum().reset_index().sort_values(by=['cylinders','origin'])
temp['rank'] = temp['weight'].groupby(temp['cylinders']).rank(ascending=1,method='dense')

# merge，根据某列匹配两个表格
df1.merge(df2, on = ["key"], how='right')
# 当左右表格键名不一致时使用
df3.merge(df4, left_on='lkey',right_on='rkey')
# concat
# 需要保证列名/行数相同
## 行连接｜列对齐
pd.concat([data1,data2,data3],keys=['data1','data2','data3'])
## 列连接｜行对齐
pd.concat([data1,data2,data3],axis =1,keys =['data1','data2','data3'])