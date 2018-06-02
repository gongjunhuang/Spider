数据分析：对已知数据进行分析，提取出有价值的信息，统计平均数、标准差等信息

数据挖掘：堆大量的数据进行分析与挖掘，得到一些未知的，有价值的信息，如从网站的用户或者用户行为数据中挖掘出用户潜在的需求信息，从而堆网站进行改善

1.定义目标

2.获取数据

3.数据搜索

4.数据预处理（数据清洗、数据集成、数据变换、数据规约）

5.挖掘建模（分类、聚类、关联、预测）

6.模型评价与发布

相关模块介绍：

1.numpy可以高效处理数据、提供数组支持，基础模块

2.pandas模块，主要用于数据探索和数据分析

3.matplotlib作图模块，解决可视化问题

4.scipy主要进行数值计算，同时支持矩阵运算，并提供了很多高等数据处理功能

5.statsmodels，主要用于统计分析

6.Gensim用于文本挖掘

7.sklearn、keras机器学习和深度学习

** pandas使用**
 
 import pandas as pd
data = pd.read_csv('E:/BaiduNetdiskDownload//hexun.csv')
data.head()

data.describe()

**data.sort_values(by='21')**

**网页中提取数据**

    import pandas as pd
    data = pd.read_html('E:\BaiduNetdiskDownload\源码\第5周\abc.html')
    data.describe()