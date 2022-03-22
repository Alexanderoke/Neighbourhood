from django.shortcuts import render,redirect
from django.contrib import auth,messages
from .forms import BussinessRegisterForm
from .models import Bussiness

# Create your views here.
def home(request):
  context={
    'title':'Home',

  }
  return render(request, 'hood/home.html',context)



def bussiness(request):
    
  
  context ={
    
    'title':'Bussiness',
    
  }
  return render(request, 'hood/bussiness.html',context)

def post(request):
    if request.method=="POST":
        form = BussinessRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Business sucessfuly Posted.")
            return redirect('bussiness')   
    else:
        messages.error(request,"Invalid Information")
        form = BussinessRegisterForm()
    context={
        "form":form}
    return render(request,'hood/post.html',context)
