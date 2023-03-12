from django.shortcuts import render,redirect
from .forms import UserForm
from .models import UserDb
from django.contrib import messages
from django.contrib.auth import authenticate
# Create your views here.
def register(request):
    if request.method=="POST":
        form=UserForm(request.POST or None)
        if form.is_valid():
            email=form.cleaned_data['email']
            obj=UserDb.objects.filter(email=email).values()
            print("email",email)
            print("obj",obj)
            if (len(obj)==1):
                messages.error(request,"Email already exits.Please register with new email")
                return render(request,'register.html')
            else:
                form.save()
                return redirect('login')
        else:
            return redirect('login')
    else:
        return render(request,'register.html')


def login(request):
    username=request.GET.get('email')
    password=request.GET.get('password')
    #result=UserDb.objects.filter(email=username,password=password).values()
    user=authenticate(email=username,password=password)
    print("user",user)
    if user is not None:
        return render(request,'navbar.html',{'user1':user})
    return render(request,'login.html')



def home(request):
    return render(request,'home.html')

def logout(request):
    return render(request,'logout.html')
