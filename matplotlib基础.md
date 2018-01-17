**绘制图形**

**折线图、散点图plot**

 x = [1, 2, 3, 5, 7]
y = [2, 3, 6, 2, 4]
plb.plot(x, y )#(x轴数据，y轴数据，展现形式)   散点图‘o’
plb.show()

cyan  青色      red    magente品红    red   blue
black    white

**pylab.show()线条样式**

-直线 --虚线  -.-.       

**点的形式**

s方形        h六角形 H    *  星号   x型   d菱形       p五角形

**轴名称**

pylab.xlabel('')       ylabel('')

**轴长度**

pylab.xlim(0, 20)    ylim()

**随机数生成**

np.random.randint(0, 20, 10)    1， 2为 范围，3 是个数

np.random.normal()     (均数，西格玛，个数)

**直方图hist**

    data3 = np.random.normal(10.0, 2.0, 100000)
    plb.hist(data3)
    plb.show()


stepfilled取消描边      style    轴的步长
    data3 = np.random.normal(10.0, 2.0, 100000)
    style = np.arange(2, 20, 2)
    plb.hist(data3, style, histtype='stepfilled')
    plb.show()

子图    subplot(2, 2, 1)  行列和当前区域

    import pandas as pd
    import matplotlib.pylab as plb
    import numpy as np
    data = pd.read_csv('E:/BaiduNetdiskDownload/hexun.csv')
    data.shape
    data.values[第几行][第几列]
    
**将某一列数据用来分析**

转置矩阵       data2= data.T     然后区某一行即可

    data2 = data.T
    y1 = data2.values[3]
    x1 = data2.values[4]
    plb.plot(x1, y1)
    plb.show()
