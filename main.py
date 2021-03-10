#IMPORTING NECESSARY LIBRARIES
from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv("irisdata.csv")

data.head()
data.tail()

X=data.iloc[:, :-1].values
y=data.iloc[:, -1].values

print(X)
print(y)