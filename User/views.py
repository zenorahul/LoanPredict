from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

#from .models import predictions, Regdb

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already Taken')
                return render(request,'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return render(request,'register.html')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,
                                              first_name=first_name,last_name=last_name)
                user.save();
                print('User created')
                return render(request,'login.html')
        else:
            # print("Password not matching")
            messages.info(request, 'Password not matching..')
            return render(request,'register.html')
        return redirect('/')
    else:
            return render(request,'register.html')


def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'pudata.html', {'first_name': username})
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def pudata(request):
    return render(request, 'pudata.html')

def prediction(request):
    if (request.method == 'POST'):
        co = request.POST['co']
        income = request.POST['income']
        amt= request.POST['amt']
        term = request.POST['term']
        credit = request.POST['credit']


        df = pd.read_csv(r"static/datasets/LoanPred.csv")
        df.dropna(inplace=True)
        df.isnull().sum()
        X_train = df[['ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History']]

        Y_train = df[['Loan_Status']]
        tree = DecisionTreeClassifier(max_leaf_nodes=6, random_state=0)
        tree.fit(X_train, Y_train)

        prediction = tree.predict([[co,income,amt,term,credit]])

        return render(request, 'prediction.html',
                      {"data": prediction, 'co': co,  'income': income,
                       'amt': amt, 'credit': credit,"term":term
                       })

    else:
        return render(request, 'prediction.html')

