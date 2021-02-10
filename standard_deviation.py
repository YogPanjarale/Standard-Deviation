import csv 
import plotly.express as px
import pandas as pd
import math
mean=0
datacsv='./data/deviation.csv'
def HandleFile():
    with open(datacsv,newline='') as f:
        reader = csv.reader(f)
        data = list(reader)[0]
        # print(data)
        # keys=data.pop(0)
        marksList= []
        marksSum=0
        for item in data:
            marks = float(item)
            marksSum+=marks
            marksList.append(marks)
        noOfEntries = len(marksList)
        mean=marksSum/noOfEntries
        print(marksList)
        calculateDeviation(marksList,mean)

        '''
        r=pd.read_csv(datacsv)
        p = px.scatter(r,x='Student Number',y='Marks')

        p.update_layout(shapes=[dict(type='line',y0=mean,y1=mean,x0=0,x1=noOfEntries)])
        p.update_yaxes(rangemode="tozero")
        # p.show()
        '''
def calculateDeviation(_list,mean):
    sl=[] #squared value list
    s=0#sum
    for i in _list:
        n=float(i)-mean
        n=n**2
        sl.append(n)
        s+=n
    d= s/(len(_list)-1)
    answer = math.sqrt(d)
    print(f'answer: {answer} \nd: {d} \nsum: {s} \nsl: {sl} \nlist: {_list} \nmean: {mean}')

HandleFile()