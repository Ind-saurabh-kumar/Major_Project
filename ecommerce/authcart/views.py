from django.shortcuts import render, redirect

# Create your views here.


def signup(request):

    if(request.method=="POST"):
        print("It is post request")
    
    else:
        print("It is get request")
    return render(request,"authentication/signup.html")


def handlelogin(request):
    return render(request, "authentication/login.html")

def handlelogout(request):
    return redirect('/authentication/login')