from django.contrib import auth, messages
from django.shortcuts import redirect, render

def home(request):
    if request.method == "POST":  # Corrected to uppercase 'POST'
        username = request.POST.get('userName')  # Using get() method to avoid KeyError
        first_three_letters = username[:3]
        password = request.POST.get('userPassword')  # Using get() method to avoid KeyError
        user_instance = auth.authenticate(username=username, password=password)
        if user_instance is not None:
            if user_instance.is_superuser:
                auth.login(request, user_instance)
                return redirect("/admin/")
            if first_three_letters == 'fin':
                auth.login(request, user_instance)
                return render (request,'fin/default_.html')
            elif  first_three_letters == 'sub':
                auth.login(request, user_instance)
                return render (request,'sub/default_.html')
            elif  first_three_letters == 'coo':
                auth.login(request, user_instance)
                return render (request,'coo/default_.html')
            elif  first_three_letters == 'std':
                auth.login(request, user_instance)
                return render (request,'std/default_.html')                        
        else:
            messages.info(request, 'Invalid credentials')  # Corrected spelling of 'messages'
            return redirect("/")
    else:
        messages.info(request, 'Invalid credentials')  # Corrected spelling of 'messages'
        return redirect("/")
    
    return render (request,'fin/default_.html')
    
def register(request):  
    
    return render (request,'register.html')
    

