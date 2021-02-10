import csv 
import plotly.express as px
import pandas as pd

mean=0
datacsv='./data/class1.csv'
with open(datacsv,newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
    keys=data.pop(0)
    marksList= []
    _min=100
    _max=0
    marksSum=0
    for item in data:
        marks = int(item[1])
        if marks >=_max:
            _max=marks
        if marks <=_min:
            _min=marks
        
        marksSum+=int(marks)
        marksList.append(marks)
    noOfEntries = len(marksList)
    mean=marksSum/noOfEntries
    print(mean)
    print(_max)
    print(_min)
    r=pd.read_csv(datacsv)
    p = px.scatter(r,x='Student Number',y='Marks')

    p.update_layout(shapes=[dict(type='line',y0=mean,y1=mean,x0=0,x1=noOfEntries)])
    p.update_yaxes(rangemode="tozero")
    # p.show()
