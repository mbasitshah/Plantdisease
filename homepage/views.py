from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'homepage.html', {'title':'Asslam o Alaikum', 'link':'http://localhost:63342/Plant-Disease-Detection-master/Templates/output.html?_ijt=o1phh3q4d2ffvdq3qso2sr0soo'})
def profile(request):
    return render(request,'homepage.html', {'title':'WalaikumAslam', 'link':'http://127.0.0.1:8000/'})
def exp(request):
    a=int(request.Get['txt1'])
    b=int(request.Get['txt2'])
    c=a+b*5
    return render(request, 'output.html', {'result':c})