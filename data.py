import pandas as pd 
import plotly.express as pe
from sklearn.cluster import KMeans
import matplotlib.pyplot as mp 
import seaborn as sb 


data = pd.read_csv("data.csv")
 
 score_train,score_test,reults_train,results_test=train_test_split(scores,results,test_size=0.25,random_state=0)

predicted_values=[]
for i in y_prediction:
    if i==0:
        predicted_values.append("authorized")
    else:
        predicted_values.append("forged")
actual_values=[]
for i in y_test:
    if i==0:
        actual_values.append("authorized")
    else:
        actual_values.append("forged")
     
Accuracy=(tn+tp)*100/(tp+tn+fp+fn)
print("accruacy:",(accuracy))

