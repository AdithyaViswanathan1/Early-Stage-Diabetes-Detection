import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from event_handlers import *
import tkinter.font as tkFont
from clean_data import *

def convert(str):
    if str == "Y" or str == "y" or str == "yes" or str == "Yes" or str == "YES":
        return 1
    if str == "N" or str == "n" or str == "no" or str == "No" or str == "NO":
        return 0

def begin(answers):
    for answer in answers:
        answer = answer.get()
        if answer != 0:
            answer = answer - 1
        #print(answer)

    new_answers = []
    for item in answers:
        if item.get() == 0:
            new_answers.append(item.get())
        else:
            item = item.get()-1
            new_answers.append(item)
    array = np.array(new_answers)
    array = array.reshape(1,-1)
    predicted = model.predict(array)
    # predicted = model.predict(x_test)
    # #print(b,c,d,e,f,g,h,i,j,k,l,m)
    print(predicted[0])

    done(predicted[0])

def done(result):
    #test cases
    message = ""
    if result == 1:
        message = "Diabetes Prediction: Positive"
    if result == 0:
        message = "Diabetes Prediction: Negative"

    fontStyle = tkFont.Font(family="Lucida Grande", size=15)
    win = tk.Toplevel()
    win.wm_title("Result")
    win.geometry("300x100")

    l = tk.Label(win, text=message, font=fontStyle)
    l.grid(row=0, column=0)

x, y = clean()

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = .2)

model = KNeighborsClassifier(n_neighbors=5)

model.fit(x_train,y_train)
accuracy = model.score(x_test, y_test)
print("Accuracy on test data: ", "{:.2f}".format(accuracy*100), "%")
#print(x_test)

questions = ["Do you have large productions or passage of urine?",
"Do you have feelings of excessive thirst?",
"Have you had a sudden loss of weight recently? ",
"Do you experience weakness frequently? ",
"Do you experience strong feelings for hunger frequently? ",
"Do you experience extreme itching frequently? ",
"Do you experience visual blurring?",
"Do you get irritated frequently and uncontrollably? ",
"Do you experience delayed healing? ",
"Do you have partial paresis (Muscular weakness caused by nerve damage)? ",
"Do you experience muscular stiffness frequently? ",
"Do you have obesity? "]

answers = []

window = tk.Tk()
window.geometry("500x1500")
fontStyle = tkFont.Font(family="Lucida Grande", size=15)
fontStyle1 = tkFont.Font(family="Lucida Grande", size=10)
greeting = tk.Label(text="Welcome to Diabates Detection Software!\n Please answer the following questions.", font=fontStyle)
greeting.pack()

for i,question in enumerate(questions):
    tk.Label(text=question,font=fontStyle1).pack(side=TOP, anchor=NW)
    answers.append(tk.IntVar())
    tk.Radiobutton(window,
                   text="Yes",
                   padx = 10,
                   variable=answers[i],
                   value=2,font=fontStyle1).pack(side=TOP,anchor=tk.NW)
    #no_answers.append(tk.IntVar())
    tk.Radiobutton(window,
                  text="No",
                  padx = 10,
                  variable=answers[i],
                  value=1,font=fontStyle1).pack(side=TOP,anchor=tk.NW)


button = tk.Button(
    text="Submit",
    width=25,
    height=25,
    command=lambda: begin(answers),
    font = fontStyle
)
button.pack()
window.mainloop()
