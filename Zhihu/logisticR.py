import pandas as pd
from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR

lessonPath = 'E:\\BaiduNetdiskDownload\\sourceCode\\week8\\lesson2.csv'
luquPath = 'E:\\BaiduNetdiskDownload\\sourceCode\\week8\\luqu2.csv'

dataLuqu = pd.read_csv(luquPath)
# 特征
x = dataLuqu.iloc[:, 1:4].as_matrix()
y = dataLuqu.iloc[:, 0:1].as_matrix()

r1 = RLR()
r1.fit(x, y)
# 特征筛选
r1.get_support()
t = dataLuqu.columns[r1.get_support()].as_matrix()

r2 = LR()
r2.fit(t, y)
print('训练结束')
print('模型正确率: '+ str(r2.score(x, y)))