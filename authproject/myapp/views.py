from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    context ={}
    return render(request,'myapp/home.html',context=context)

def contacts(request):
    context ={}
    return render(request,'myapp/contacts.html',context=context)

def data_security(request):
    context ={}
    return render(request,'myapp/data_security.html',context=context)

def liscence_policy(request):
    context ={}
    return render(request,'myapp/liscence_policy.html',context=context)

def user_aggrement(request):
    context ={}
    return render(request,'myapp/user_aggrement.html',context=context)

@login_required
def dashboard(request):
    context ={}
    return render(request,'myapp/dashboard.html',context=context)