from django.shortcuts import render, HttpResponse
from Home.myMod import HeyClass
obj = HeyClass()
from model import *
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0,1))


def home(request):
    # print(f"this is just test {test_list}")
    # loaded_model = pickle.load(open('pickletest1.pkl','rb'))
    # print(f"THIsis send list {send_ls}")
    # print(f"this is the predicted values {loaded_model.predict(send_ls)}")
    return render(request, 'index.html')

def jobs(request):
    return render(request, 'jobs.html', {"result" : obj.fun()})

def admissions(request):
    return render(request, 'admissions.html')

def job_pred(request):
    if request.method == 'POST':
        region = request.POST['region']
        state = request.POST['state']
        course = request.POST['branch']
        loaded_model = pickle.load(open('pickletest1.pkl','rb'))
        # data = pd.read_csv('dataFinal.csv')
        # data = pd.DataFrame(data)
        years = [2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
        u=data.loc[(data['BRANCH']==course) & (data['LOC_STATE']==state) & (data['LOC_REGION']==region)]
        o=[]
        for i in years:
            y=u.loc[u['YEAR']==i].shape[0]
            o.append(y*98) 
        h=[]
        for i in range(5):
            f=np.array(o[-3:],dtype='object')
            f=f.reshape(-1,1)
            scaled_f= sc.fit_transform(f)
            scaled_f=scaled_f.reshape(1,3,1)
            predicted_f= loaded_model.predict(scaled_f)
            bhu=sc.inverse_transform(predicted_f)
            h.append(int(bhu))
            o.append(int(bhu))
            h=list(h)
        print(o)
        return HttpResponse(o)
    return HttpResponse("GEt")

def adm_pred(request):
    if request.method == 'POST':
        print(request.POST['location'])
        return HttpResponse(request.POST['location'])
    return HttpResponse("GET")

def impfun(request):
    out = final()
