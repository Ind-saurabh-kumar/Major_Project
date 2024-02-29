from django.shortcuts import render, redirect, HttpResponse

from django.contrib.auth.models import User

from django.contrib import messages

# Create your views here.


def signup(request):

    if request.method == "POST":
        email=request.POST['email']
        password = request.POST['pass1']
        confirm_password=request.POST['pass2']

        if password != confirm_password:
           messages.warning(request, "Password is Not Matching")
           return render(request,'signup.html')
        
        try:
            if User.objects.get(User==email):
                messages.info(request, "Email Already Exist")
                return render(request,'signup.html')
        except Exception as identifier:
            pass
        
        user = User.objects.create_user(email, email, password)
        user.save()
        messages.success(request, "Account Created Successfully")
        return render(request,'signup.html')
    
    return render(request,"signup.html")


def handlelogin(request):
    return render(request, "login.html")

def handlelogout(request):
    return redirect('login.html')