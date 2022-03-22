from django.shortcuts import render
from .forms import BussinessRegisterForm
from .models import Bussiness

# Create your views here.
def home(request):
  context={
    'title':'Home',

  }
  return render(request, 'hood/home.html',context)



def bussiness(request):
  form = BussinessRegisterForm(request.POST,request.FILES)
  if form.is_valid():    
    form.save()
  context ={
    'form':BussinessRegisterForm(),
    'title':'Bussiness',
    'posts':Bussiness.objects.all()
  }
  return render(request, 'hood/bussiness.html',context)
