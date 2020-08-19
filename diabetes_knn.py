import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing
import matplotlib.pyplot as pyplot
from matplotlib import style

def convert(str):
    if str == "Y" or str == "y" or str == "yes" or str == "Yes" or str == "YES":
        return 1
    if str == "N" or str == "n" or str == "no" or str == "No" or str == "NO":
        return 0
data = pd.read_csv("diabetes_data_upload.csv")
data = data.drop(columns="Genital thrush")
data = data.drop(columns="Alopecia")
#print(data.head())

#Gender,Polyuria,Polydipsia,sudden weight loss,weakness,Polyphagia,Genital thrush,
#visual blurring,Itching,Irritability,delayed healing,partial paresis,muscle stiffness,
#Alopecia,Obesity,class
le = preprocessing.LabelEncoder()
age = list(data["Age"])
gender = le.fit_transform(list(data["Gender"]))
polyuria = le.fit_transform(list(data["Polyuria"]))
polydipsia = le.fit_transform(list(data["Polydipsia"]))
weight_loss = le.fit_transform(list(data["sudden weight loss"]))
polyphagia = le.fit_transform(list(data["Polyphagia"]))
#genital_thrush = le.fit_transform(list(data["Genital thrush"]))
visual_blur = le.fit_transform(list(data["visual blurring"]))
itch = le.fit_transform(list(data["Itching"]))
irritable = le.fit_transform(list(data["Irritability"]))
delayed_healing = le.fit_transform(list(data["delayed healing"]))
paresis = le.fit_transform(list(data["partial paresis"]))
muscle_stiff = le.fit_transform(list(data["muscle stiffness"]))
#alopecia = le.fit_transform(list(data["Alopecia"]))
obesity = le.fit_transform(list(data["Obesity"]))
cls = le.fit_transform(list(data["class"]))
#print("gender: ", gender, "polyuria: ", polyuria)

predict = "cls"

x = list(zip(gender,polyuria,polydipsia,weight_loss,polyphagia,visual_blur,itch,irritable,delayed_healing,paresis,muscle_stiff,obesity))
y = list(cls)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = .2)

model = KNeighborsClassifier(n_neighbors=3)

model.fit(x_train,y_train)
accuracy = model.score(x_test, y_test)
print("Accuracy on test data: ", "{:.2f}".format(accuracy*100), "%")
#print(x_test)

a = input("Gender (M or F): ")
if(a == "M" or "m"):
    a = 1
else:
    a = 0

#Gender,Polyuria,Polydipsia,sudden weight loss,weakness,Polyphagia,Genital thrush,
#visual blurring,Itching,Irritability,delayed healing,partial paresis,muscle stiffness,
#Alopecia,Obesity,class

b = input("Do you have large productions or passage of urine (Y or N)? ")
b = convert(b)
#print("1 or 0",b)

c = input("Do you have feelings of excessive thirst (Y or N)? ")
c = convert(c)

d = input("Have you had a sudden loss of weight recently (Y or N)? ")
d = convert(d)

e = input("Do you experience weakness frequently (Y or N)? ")
e = convert(e)

f = input("Do you experience strong feelings for hunger frequently (Y or N)? ")
f = convert(f)

g = input("Do you experience extreme itching frequently (Y or N)? ")
g = convert(g)

h = input("Do you experience visual blurring (Y or N)? ")
h = convert(h)

i = input("Do you get irritated frequently and uncontrollably (Y or N)? ")
i = convert(i)

j = input("Do you experience delayed healing (Y or N)? ")
j = convert(j)

k = input("Do you have partial paresis (Muscular weakness caused by nerve damage) (Y or N)? ")
k = convert(k)

l = input("Do you experience muscular stiffness frequently (Y or N)? ")
l = convert(l)

m = input("Do you have obesity (Y or N)? ")
m = convert(m)

predicted = model.predict([[b, c, d, e, f, g, h, i, j, k, l, m]])
#predicted = model.predict(x_test)
print(b,c,d,e,f,g,h,i,j,k,l,m)
print(predicted[0])

#test cases
#No,Yes,No,Yes,No,No,Yes,No,Yes,No,Yes,Yes,Positive
#Male,Yes,No,No,No,Yes,Yes,Yes,No,Yes,Yes,Yes,No,Negative
if predicted[0] == 1:
    print("Diabetes Prediction: Positive")
if predicted[0] == 0:
    print("Diabetes Prediction: Negative")