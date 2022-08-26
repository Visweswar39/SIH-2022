from django.shortcuts import render, HttpResponse
from Home.myMod import HeyClass
obj = HeyClass()
from model import *
import pickle
import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
sc = MinMaxScaler(feature_range = (0,1))


def home(request):
    # print(f"this is just test {test_list}")
    # loaded_model = pickle.load(open('pickletest1.pkl','rb'))
    # print(f"THIsis send list {send_ls}")
    # print(f"this is the predicted values {loaded_model.predict(send_ls)}")
    return render(request, 'index.html')

def jobs(request):
    return render(request, 'jobs.html', {"result" : obj.fun()})


def graph(y):
    x = ["Enrolled percentage","placement percentage","Employement potential"]
    trace = go.Bar(x=x,y=y,width=0.5,marker={'color':'chocolate'})
    data = [trace]
    layout=go.Layout(xaxis={'title':'parameter'},yaxis={'title':'percentage'})
    fig = go.Figure(data=data,layout=layout)
    z=pyo.plot(fig,output_type='div')
    return z

mapping = {
    "GVP" : graph([94.45,38.17,39.91]),
    "ANITS" : graph([97.89,36.69,40.94]),
    "BABA" : graph([63.78,20.84,32.06]),
    "DIET" : graph([66.26,15.67,23.63]),
    "AVANTI" : graph([54.87,11.69,21.79]),
    "VIIT" : graph([55.23,21.30,38.21]),
    "Sundar Rajan" : graph([91.93,51.08,55.56]),
    "PEC" : graph([84,50.11,58.47]),
    "St.Xavier's" : graph([92,60.56,66.91])

}
def admissions(request):
    if request.method == 'POST':
        return render(request,'graph.html',{"result": mapping[request.POST['college']], "cname":request.POST['college'], "cloc":request.POST['location'], "cbranch":request.POST['branch']})
        # return render(request, 'admissions.html', {"  result": mapping[request.POST['college']], "cname":request.POST['college'], "cloc":request.POST['location'], "cbranch":request.POST['branch']})
    return render(request,'admissions.html', {"result":''})

def job_pred(request):
    if request.method == 'POST':
        region = request.POST['region']
        state = request.POST['state']
        course = request.POST['branch']
        loaded_model = pickle.load(open('pickletest1.pkl','rb'))
        gtitle = "Scope of getting jobs in {} region, {}, in {} department".format(region, state, course)
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
        # print(o)
        # x_pred = [2022,2023,2024,2025,2026]
        # fig = plt.figure()
        # fig.set_figwidth(10)
        # fig.set_figheight(5)
        # plt.plot(years,o[:-5])
        # plt.plot(x_pred,h)
        # plt.xticks(years+x_pred,years+x_pred)
        #plt.show()
        av1=sum(o[:-5])
        av1//=11
        av2=sum(h)
        av2//=5
        if(av1>av2):
            #print('k')
            msg = "Scope of getting job in this domain is considerably depreciating"
        else:
            #print('l')
            msg = "Scope of getting job in this domain in future is higher"
        print(type(o))
        x1 = ["2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021"]
        x2 = ["2022","2023","2024","2025","2026"]
        trace1 = go.Scatter(x=x1,y=o[:12],mode='lines+markers',marker={'color':"red"},name='past')
        trace2 = go.Scatter(x=x2,y=o[12:],mode='lines+markers',marker={'color':"blue"},name = 'predicted')
        d = [trace1,trace2]
        layout = go.Layout(xaxis={'title':'year'},yaxis={'title':'number of obtained jobs'})
        fig  = go.Figure(data=d,layout=layout)
        l = pyo.plot(fig,output_type='div')
        return render(request,'graph.html',{"graph":l, "message":msg, "gtitle":gtitle})

    return HttpResponse("GEt")

def fyj(request):
    if request.method == 'POST':
        if request.POST['role'] == 'A':
            context={
             "skills":['s1','s2','s3']   
            }
        elif request.POST['role'] == 'B':
            context={
             "skills":['s4','s5','s6']   
            }
        elif request.POST['role'] == 'C':
            context={
             "skills":['s11','s12','s13']   
            }
        elif request.POST['role'] == 'D':
            context={
             "skills":['s14','s15','s16']   
            }
        return render(request,'findjob.html',context)
    return render(request,'findjob.html')

di1 = {}
di1['sde'] = ['DSA','CPP / JAVA','PROBLEM SOLVING','OPERATING SYSTEMS','DBMS']
di1['web_developer'] = ['DNS MANAGEMENT', 'WIRE FRAMES', 'DEBUGGING', 'VISUAL THINKING']
di1['AI_Engineer'] = ['AWS', 'EDA', 'SECURITY DEPLOYMENT']
di1['Electronics_Design_Engineer'] = ['HARDWARE KNOWLEDGE', 'TESTING KNOWLEDGE', 'CRITICAL THINKING']
di1['Field_Test_Engineer'] = ['TEST SCRIPTS', 'DATA COLLECTION', 'RADIO FREQUENCY']
di1['Telecom_Engineer'] = ['POWER ELECTRONICS', 'OPTICAL FIBER COMMUNICATION', 'MICROPROCESSOR', 'CONTROL SYSTEM']
di1['Broadcast_Engineer'] = ['AUDIO ENGINNERING', 'ARV INSTRUMENTATION', 'COMPUTER ENGINEERING']
di1['Systems_Engineer'] = ['DETAILED ORIENTED THINKING', 'TROUBLE SHOOTING', 'ANALYTICAL SKILLS']
di1['Material_Engineer'] = ['FRACTURE TOUGHNESS', 'CREEP DEFORMATION']
di1['Petroleum_Engineer'] = ['THERMODYNAMICS', 'GEOLOGY OF PETROLEUM', 'GEOMECHANICS']
di1['Chemical_Engineer'] = ['ENVIRONMENTAL SCIENCE', 'PROCESS DYNAMICS AND CONTROL', 'ORGANIC CHEMICAL TECHNOLOGY', 'PLASTIC ENGINEERING']
di1['Automative_Engineer'] = ['R ', 'ISO', 'CAD']
di1['Thermal_Engineer'] = ['HEAT TRANSFER', 'FLUID MECHANICS', 'THERMAL MATERIALS']
di1['Manufacturing_Engineer'] = ['PRODUCTION AND PROCESSING', 'MECHANICAL DESIGN']
di1['Construction_Engineer'] = ['MATLAB', 'GIS','CAD']
di1['Urban_Planning_Engineer'] = ['GIS', 'ARCGIS', 'SITE PLANS','CAD']
di1['Architect'] = ['ADVANCED MATH', 'DESIGN SKILLS', 'COMPUTER LITERACY', 'BUSINESS KNOWLEDGE']
di = {}
di['sde'] = 'Software engineering is the branch of computer science that deals with the design, development, testing, and maintenance of software applications. Software engineers apply engineering principles and knowledge of programming languages to build software solutions for end users.'
di['web_developer'] = 'A website engineer is a computer and technology professional who builds websites and applications. Using computer coding skills, they can create web applications and destinations that meet user needs. They can also maintain these applications and monitor them to ensure that their functionality remains intact.'
di['AI_Engineer'] = 'Artificial intelligence engineers are individuals who use AI and machine learning techniques to develop applications and systems that can help organizations increase efficiency, cut costs, increase profits, and make better business decisions.'
di['Electronics_Design_Engineer'] = 'Electronics engineers design and develop electronic equipment, including broadcast and communications systems, such as portable music players and Global Positioning System (GPS) devices. Many also work in areas closely related to computer hardware.'
di['Field_Test_Engineer'] = 'Field engineer duties usually include inspecting and installing equipment and new technologies, directing crews or workers on site, conducting research, and reporting on project status. Field engineers will make sure that everything works smoothly and engineering designs are being followed.'
di['Telecom_Engineer'] = 'A telecommunication engineer is responsible for designing and overseeing the installation of telecommunications equipment and facilities, such as complex electronic switching systems, and other plain old telephone service facilities, optical fiber cabling, IP networks, and microwave transmission systems.'
di['Broadcast_Engineer'] = 'Broadcast engineers are responsible for the strength, clarity, and overall quality of sounds and images broadcast on radio and television, and—increasingly—sound and image transmitted via satellite, cable, and the internet.'
di['Systems_Engineer'] = 'Systems engineers develop and oversee all aspects of a complex system to solve a problem, from the initial creation of the system to production and management through the end product or solution.'
di['Material_Engineer'] = 'Materials engineers work with metals, ceramics, and plastics to create new materials. Materials engineers develop, process, and test materials used to create a range of products, from computer chips and aircraft wings to golf clubs and biomedical devices.'
di['Petroleum_Engineer'] = "Petroleum engineers help find oil and gas for the country's energy needs. Petroleum engineers design and develop methods for extracting oil and gas from deposits below the Earth's surface. Petroleum engineers also find new ways to extract oil and gas from older wells"
di['Chemical_Engineer'] = 'Chemical engineers develop and design chemical manufacturing processes. Chemical engineers apply the principles of chemistry, biology, physics, and math to solve problems that involve the production or use of chemicals, fuel, drugs, food, and many other products.'
di['Automative_Engineer'] = ' An automotive engineer works with other engineers to design and test brake systems, engines, fuel technologies and transmissions within a vehicle. Automotive engineers use software programs and other machine tools to design and test automotive systems for applicable vehicles.'
di['Thermal_Engineer'] = 'Thermal engineering is a constituent subdiscipline of Mechanical engineering that deals with the planning and designing of heating and cooling systems as well as with the maintenance of these heating and cooling systems'
di['Manufacturing_Engineer'] = "Manufacturing engineering is a branch of engineering that focuses on improving the production of an item, whether that's through making product design changes or creating more effective manufacturing processes"
di['Construction_Engineer'] = "Construction Engineering is a professional discipline that deals with the designing, planning, construction, and management of infrastructures such as roads, tunnels, bridges, airports, railroads, facilities, buildings, dams, utilities and other projects."
di['Urban_Planning_Engineer'] = "An urban planner is someone who develops plans and programs for the use of land. They plan to create communities, accommodate growth, or revitalize physical facilities in towns, cities, counties, and metropolitan areas."
di['Architect'] = "An architect is a person who plans, designs and oversees the construction of buildings. To practice architecture means to provide services in connection with the design of buildings and the space within the site surrounding the buildings that have human occupancy or use as their principal purpose."
links=pd.read_excel('/home/subhani/Desktop/SIH/Final/links.xlsx')
addresses=pd.read_excel('/home/subhani/Desktop/SIH/Final/addresses.xlsx')

def fds(request):
    if request.method == 'POST':
        region = request.POST['state']
        role = request.POST['role']
        l=di1[role]
        s=[]
        s1=[]
        a=addresses.loc[(addresses['LOCATION']==region)]
        for x in l:
            b=a.loc[a['SKILL']==x]
            s.append(b.iloc[0,2])
            c=links.loc[links['SKILL']==x]
            s1.append(c.iloc[0,1])

        print(l,s,s1)
        obj = []
        desc=di[role]
        for i in range(len(l)):
            lo=[]
            lo.append(l[i])
            lo.append(s[i])
            lo.append(s1[i])
            obj.append(lo)
        print(obj)
        context = {
            "skills":l,
            "addresses":s,
            "resources":s1,
            "obj":obj,
            "desc":desc,
        }
        for o in obj:
            print(o[0])
            print(o[1])
            print(o[2])
        return render(request,'list.html', context)
    return render(request,'findjob.html')


def test(request):
    return render(request,"basef.html")