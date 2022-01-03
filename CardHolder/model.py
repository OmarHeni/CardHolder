import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

data=pd.read_excel('default_of_credit_card_clients.xls')

def My_function(data_c):
    list_results = list()
    for i, row in data_c.iterrows():
        items = row[6:12].tolist()
        a_set = set(items)
        number_of_unique_values = len(a_set)
        if (number_of_unique_values > 2):
            list_results.append(i)

    for l in list_results:
        data_c.drop(l, inplace=True)
    return data_c
data.rename(columns={'default payment next month':'dpnm'}, inplace=True)
data.rename(columns={'PAY_0':'PAY_1'}, inplace=True)

pay_x = ['PAY_1', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6']
data['pay_x']= data[pay_x].mean(axis=1)

X = data.drop(['dpnm'], axis=1)
y = data.dpnm

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)


data = My_function(data)
pay_x = ['PAY_1', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6']

data['Status'] =  np.where((data['PAY_1']<=0) & (data['PAY_2']<=0) & (data['PAY_3']<=0) & (data['PAY_4']<=0) & (data['PAY_5']<=0) & (data['PAY_6']<=0) ,0,2)
data.loc[(data['PAY_1']!=-1) & (data['PAY_2']!=-1) & (data['PAY_3']!=-1) & (data['PAY_4']!=-1) & (data['PAY_5']!=-1) & (data['PAY_6']!=-1) ,'Status']=1


rfc =  RandomForestClassifier(random_state=0)
rfc.fit(X_train,y_train)
print("Score du modèle : %.2f" % rfc.score(X_test, y_test))


filename = 'finalized_model.sav'
joblib.dump(rfc,filename)