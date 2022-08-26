import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from sklearn.ensemble import RandomForestRegressor
city = 'Visakhapatnam'
course = 'Computer Science and Technology'
def classify(city,course,dataframe):
    main_df=dataframe.loc[dataframe['CITY'].str.contains('Visakhapatnam') & dataframe['COURSE'].str.contains('Computer Science and Technology')]
    return main_df

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

rand_clf1=RandomForestRegressor(n_estimators = 1000,max_features='sqrt')
rand_clf1.fit(X_train1,y_train1)
rand_clf2=RandomForestRegressor(n_estimators = 1000,max_features='sqrt')
rand_clf2.fit(X,y)

data = pd.read_excel("C:\\Users\\Viswes\\hackathon\\AICTE3 datasets\\AICTE3 test.xlsx")

def testpreprocessing(city,course,data):

    dftest=classify(city,course,data)
    dftest.drop(['CITY','CITY ID','LEVEL','PROGRAMME','COURSE','COURSE ID','STATE ','PLACED STUDENTS','CUTOFF RANK'],axis=1,inplace=True)
    X_test1 = dftest.iloc[:,0:4]
    y_test1 = dftest.iloc[:,4]


    df1=classify(city,course,data)
    df1.drop(['CITY','CITY ID','LEVEL','PROGRAMME','COURSE','COURSE ID','STATE '],axis=1,inplace=True)
    X1 = df1.iloc[:,0:5]
    y1 = df1.iloc[:,5]

    emp_potential_real = df1['PLACED STUDENTS']/df1['ENROLLED STUDENTS']  
    yrand_pred1,yrand_pred=prediction(rand_clf1,rand_clf2,X_test1,X1)  
    employement_potential(yrand_pred1,yrand_pred)
    return X_test1,y_test1,X1,y1,emp_potential_real



def prediction(rand_clf1,rand_clf2,X_test1,X1):
    yrand_pred=rand_clf1.predict(X_test1)
    yrand_pred1=rand_clf2.predict(X1)
    print("predicted admissions for the year is ",yrand_pred)
    print("predicted placements for the college is",yrand_pred1)
    return yrand_pred1,yrand_pred


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

testpreprocessing(city,course,data)