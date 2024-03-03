from django.http import HttpResponse
from django.shortcuts import render

def log(request):
    return render(request,'index.html')
def form(request):
    
    new = request.POST['pw']
    if new == '1234':
        name = request.POST['name'] 
        x = 'login.html'
        return render(request,x ,{'name':name})
    else:
        return render(request,'error.html') 