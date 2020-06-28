from django.http import HttpResponse
from django.shortcuts import render
import pyrebase
from getpass import getpass


firebaseConfig = {
    "apiKey": "AIzaSyAjWJS8oNvnEh2neDdbXNxRwKgu5IRl9uw",
    "authDomain": "webdevelopement-d0d0b.firebaseapp.com",
    "databaseURL": "https://webdevelopement-d0d0b.firebaseio.com",
    "projectId": "webdevelopement-d0d0b",
    "storageBucket": "webdevelopement-d0d0b.appspot.com",
    "messagingSenderId": "533022133930",
    "appId": "1:533022133930:web:96901018ad27c4f99c8ad3",
    "measurementId": "G-PC270YQWWP"




}   
firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth() 

def login(request):
    return render(request,'index.html')

def user(request):
    email = request.GET.get('ipusername')
    password = request.GET.get('ippassword')
    print(email)
    print(password)
    try:
        auth.sign_in_with_email_and_password(email,password)
        return render(request,'loginsuccess.html')
    except:
        return HttpResponse('Invalid Data')

def faizpics(request):
    return render(request,'faizpics.html')