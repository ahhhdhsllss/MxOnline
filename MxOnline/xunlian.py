import pandas as pd
import numpy as np
import csv
train=pd.read_csv('verify.csv',engine='python',encoding="utf8")
test=pd.read_csv('test.csv',engine='python',encoding="utf8")

#分别获取训练数据和标签
X_train_data=train.drop(columns=["flag", "控制人ID"])
y_train_data=train['flag']

from xgboost import XGBClassifier

model = XGBClassifier(learning_rate=0.3,      #含义：学习率，控制每次迭代更新权重时的步长，默认0.3。
                      n_estimators=1000,         # 含义：总共迭代的次数，即决策树的个数
                      max_depth=8,               # 树的深度,值越大，越容易过拟合；值越小，越容易欠拟合。
                      min_child_weight = 4,      # 值越大，越容易欠拟合；值越小，越容易过拟合（值较大时，避免模型学习到局部的特殊样本）
                      gamma=0.1,                  # 惩罚项系数，指定节点分裂所需的最小损失函数下降值
                      subsample=0.8,             # 随机选择80%样本建立决策树
                      colsample_btree=0.8,       # 随机选择80%特征建立决策树
                      objective='multi:softmax',  # 指定损失函数
                      scale_pos_weight=0.425,        # 正样本的权重，在二分类任务中，当正负样本比例失衡时，设置正样本的权重，模型效果更好。例如，当正负样本比例为1:10时，scale_pos_weight=10。
                      random_state=27         # 随机数)
                      )

model.fit(X_train_data, y_train_data)
y_pred = model.predict(test)
sum_0 = 0
sum_1 = 0
for y in y_pred:
    if y >=0.5:
        sum_0 += 1
    else:
        sum_1 += 1
print(sum_0)
print(sum_1)

f = open('result.csv','w+',encoding='gb18030',newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(["flag"])
y_pred = list(map(lambda x: [x], y_pred))
for y in y_pred:
    csv_writer.writerow(y)
y_flag = pd.read_csv('result.csv', encoding="gbk")
print(y_flag.shape[0])

y_id = test['ID']
result = pd.concat([y_id,y_flag],axis=1)
result.to_csv("结果集.csv")










