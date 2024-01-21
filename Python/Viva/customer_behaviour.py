# /Users/1to3for5vi7ate9x/Downloads/marketing_campaign.csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv('Social_Network_Ads.csv')
X = dataset.iloc[:, 2:4].values
y = dataset.iloc[:, -1].values
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0) 
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
print(X_train)
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test) 
print(np.concatenate((y_pred.reshape(len(y_pred),1),y_test.reshape(len(y_test),1)),1)) 
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)
age=int(input("Enter the age: "))
salary = int(input("Enter the estimated salary: "))
result = classifier.predict(sc.transform([[age,salary]]))
print(result)
if result==[1]:
    print("Yay! This customer can buy a car!") 
else:
    print("Sorry! It seems this customer won't buy a car")