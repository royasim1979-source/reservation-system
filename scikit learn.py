import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
le = LabelEncoder()
d = {"Age":[1,2,3,4,5],"salary":[100,200,300,400,500],"purchased":["No","No","Yes","No","Yes"]}
df = pd.DataFrame(d)
mean = df["Age"].mean()
print(mean)
#data = df["Age"].fillna(mean)
# print(data)
df["purchased"] = le.fit_transform(df["purchased"])
#df = pd.get_dummies(df,columns=["purchased"])
#print(df)
x =df[["Age","salary"]]
scalar = StandardScaler()
x_scale = scalar.fit_transform(x)
#print(x_scale)
a = df[["Age","salary"]]
b = df["purchased"]
a_train,a_test,b_train,b_test = train_test_split(a,b,test_size = 0.1,random_state=42)
model = LinearRegression()
model.fit(a_train,b_train)
y_pred = model.predict(a_test)
print(model.coef_)
print(model.intercept_)
print(b_test.values)
print(y_pred)



plt.scatter(a_train.iloc[:,0],b_train,color="red")

plt.xlabel("age")
plt.ylabel("salary")
plt.title("linear regression")
plt.show()
