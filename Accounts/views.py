from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.views import View

from ProductItem.models import Customer
from .forms import RegistrationForm,CustomerProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.


class RegistrationView(View):
    def get(self,request):
        form=RegistrationForm()
        return render(request,'Accounts/register.html',{'form':form})
    def post(self,request):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations!! Registered Successfully')
            form.save()
        return render(request,'Accounts/register.html',{'form':form})
    

@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    def get(self,request):
        form= CustomerProfileForm()
        return render(request,'Accounts/profile.html',{'form':form , 'active':'btn-primary'})
    
    def post(self,request):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            usr=request.user
            name=form.cleaned_data['name']
            phone=form.cleaned_data['phone']
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            district=form.cleaned_data['district']
            gender=form.cleaned_data['gender']
            reg=Customer(user=usr,name=name,phone=phone,locality=locality,city=city,district=district,gender=gender)
            reg.save()
            messages.success(request,'Congratulation!! Your Profile Updated Successfully')
        return render(request,'Accounts/profile.html',{'form':form , 'active':'btn-primary'})

@login_required
def Address(request):
    add=Customer.objects.filter(user=request.user)
    return render(request, 'Accounts/address.html',{'add':add , 'active':'btn-primary'})


