def classify(city,course,dataframe):
    main_df=dataframe.loc[dataframe['CITY'].str.contains('Visakhapatnam') & dataframe['COURSE'].str.contains('Computer Science and Technology')]
    return main_df


import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from sklearn.ensemble import RandomForestRegressor

def preprocessing(city,course):
    dftrain = pd.read_excel("C:\\Users\\Viswes\\hackathon\\AICTE3 datasets\\AICTE train.xlsx")
    dftrain=classify(city,course,dftrain)
    dftrain.drop(['CITY','CITY ID','LEVEL','PROGRAMME','COURSE','COURSE ID','STATE ','PLACED STUDENTS','CUTOFF RANK'],axis=1,inplace=True)
    X_train1 = dftrain.iloc[:,0:4]
    y_train1 = dftrain.iloc[:,4]

    df = pd.read_excel("C:\\Users\\Viswes\\hackathon\\AICTE3 datasets\\AICTE train.xlsx")
    df=classify(city,course,df)
    df.drop(['CITY','CITY ID','LEVEL','PROGRAMME','COURSE','COURSE ID','STATE '],axis=1,inplace=True)
    X = df.iloc[:,0:5]
    y = df.iloc[:,5]

    return X_train1,y_train1,X,y




def training(X_train1,y_train1,X,y):
    rand_clf1=RandomForestRegressor(n_estimators = 1000,max_features='sqrt')
    rand_clf1.fit(X_train1,y_train1)
    rand_clf2=RandomForestRegressor(n_estimators = 1000,max_features='sqrt')
    rand_clf2.fit(X,y)

    return rand_clf1,rand_clf2


def testpreprocessing(city,course):
    dftest = pd.read_excel("C:\\Users\\Viswes\\testingtest.xlsx")
    dftest=classify(city,course,dftest)
    dftest.drop(['CITY','CITY ID','LEVEL','PROGRAMME','COURSE','COURSE ID','STATE ','PLACED STUDENTS','CUTOFF RANK'],axis=1,inplace=True)
    X_test1 = dftest.iloc[:,0:4]
    y_test1 = dftest.iloc[:,4]

    df1 = pd.read_excel("C:\\Users\\Viswes\\testingtest.xlsx")
    df1=classify(city,course,df1)
    df1.drop(['CITY','CITY ID','LEVEL','PROGRAMME','COURSE','COURSE ID','STATE '],axis=1,inplace=True)
    X1 = df1.iloc[:,0:5]
    y1 = df1.iloc[:,5]

    emp_potential_real = df1['PLACED STUDENTS']/df1['ENROLLED STUDENTS']

    return X_test1,y_test1,X1,y1,emp_potential_real


def prediction(rand_clf1,rand_clf2,X_test1,X1):
    yrand_pred=rand_clf1.predict(X_test1)
    yrand_pred1=rand_clf2.predict(X1)
    
    return yrand_pred,yrand_pred1


def errors(yrand_pred,yrand_pred1,y_test1,y1):
    print('mae=',mean_absolute_error(y_test1,yrand_pred))
    print('mse=',mean_squared_error(y_test1,yrand_pred))
    print('r2_score=',r2_score(y_test1,yrand_pred))

    print('mae=',mean_absolute_error(y1,yrand_pred1))
    print('mse=',mean_squared_error(y1,yrand_pred1))
    print('r2_score=',r2_score(y1,yrand_pred1))

def employement_potential(yrand_pred1,yrand_pred):
    emp_potential = yrand_pred1/yrand_pred
    print('\n')
    print("Employement potential if student studied in this college is ",emp_potential,"\n")
    print("Employement potential of the branch in given demographic location will be ",emp_potential.mean(),"\n")
    return emp_potential

def employement_potential_error(emp_potential_real,emp_potential):
    print(mean_absolute_error(emp_potential_real,emp_potential))



X_train1,y_train1,X,y=preprocessing('Visakhapatnam','Computer Science and Technology')
rand_clf1,rand_clf2=training(X_train1,y_train1,X,y)
X_test1,y_test1,X1,y1,emp_potential_real=testpreprocessing('Visakhapatnam','Computer Science and Technology')
yrand_pred,yrand_pred1=prediction(rand_clf1,rand_clf2,X_test1,X1)
emp_potential=employement_potential(yrand_pred1,yrand_pred)
employement_potential_error(emp_potential_real,emp_potential)

errors(yrand_pred,yrand_pred1,y_test1,y1)







'''dftest = pd.read_excel("C:\\Users\\Viswes\\hackathon\\AICTE3 datasets\\AICTE3 test.xlsx")
dftest.drop(['CITY','CITY ID','LEVEL','PROGRAMME','COURSE','COURSE ID','STATE ','PLACED STUDENTS'],axis=1,inplace=True)
X_test1 = dftest.iloc[:,0:4]
y_test1 = dftest.iloc[:,4]

#random forests
rand_clf=RandomForestRegressor(n_estimators = 1000,max_features='sqrt')

yrand_pred=rand_clf.predict(X_test1)



df1 = pd.read_excel("C:\\Users\\Viswes\\hackathon\\AICTE3 datasets\\AICTE3 test.xlsx")
df1.drop(['CITY','CITY ID','LEVEL','PROGRAMME','COURSE','COURSE ID','STATE '],axis=1,inplace=True)

X1 = df1.iloc[:,0:5]
y1 = df1.iloc[:,5]
#random forests

yrand_pred1=rand_clf.predict(X1)


emp_potential = yrand_pred1/yrand_pred
emp_potential_real = df1['PLACED STUDENTS']/df1['ENROLLED STUDENTS']
emp_potential.mean()
emp_potential_real.mean()
print(mean_absolute_error(emp_potential_real,emp_potential))
'''
