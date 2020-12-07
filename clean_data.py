import pandas as pd
from sklearn import preprocessing

def clean():
    data = pd.read_csv("diabetes_data.csv")
    data = data.drop(columns="Genital thrush")
    data = data.drop(columns="Alopecia")
    #print(data.head())

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

    return x,y
