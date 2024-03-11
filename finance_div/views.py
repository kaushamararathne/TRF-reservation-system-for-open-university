from django.shortcuts import redirect, render

def tests(request):     
    context = {
        'mode':"Financial Division",
        'name':"user",
    }
    return render (request,'fin/home.html',context)
