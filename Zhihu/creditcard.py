import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cross_validation import train_test_split, KFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, recall_score, classification_report

data = pd.read_csv("E:\\BaiduNetdiskDownload\\sourceCode\\week8\\creditcard.csv")
# print(data.head())
def plotData():
    count_classes = pd.value_counts(data['Class'], sort=True).sort_index()
    count_classes.plot(kind='bar')
    plt.title("Fraud class histogram")
    plt.xlabel("Class")
    plt.ylabel("Frequency")
    plt.show()

# 下采样和过采样
X = data.iloc[:, data.columns != 'Class']
Y = data.iloc[:, data.columns == 'Class']

number_records_fraud = len(data[data.Class == 1])
fraud_indices = np.array(data[data.Class == 1].index)

normal_indices = data[data.Class == 0].index
random_normal_indices = np.random.choice(normal_indices, number_records_fraud, replace=False)
random_normal_indices = np.array(random_normal_indices)

# 将随机正常的数据同诈骗数据合并到一起
under_sample_indices = np.concatenate([fraud_indices, random_normal_indices])
under_sample_data = data.iloc[under_sample_indices, :]

X_under_sample = under_sample_data.ix[:, under_sample_data.columns != 'Class']
Y_under_sample = under_sample_data.ix[:, under_sample_data.columns == 'Class']

print("Percentage of normal transactions: ", len(under_sample_data[under_sample_data.Class == 0])/len(under_sample_data))
print("Percentage of fraud transactions: ", len(under_sample_data[under_sample_data.Class == 1])/len(under_sample_data))
print("Total number of transactions in resampled data: ", len(under_sample_data))

