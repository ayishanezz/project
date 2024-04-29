from django.shortcuts import render,redirect
from django.views import View
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views.generic import CreateView,FormView,TemplateView



# # Create your views here.
# class LandingView(View):
#     def get(self,request):
#         return render(request,"landing.html")

class LandingView(TemplateView):
    template_name="landing.html"

    
# class LoginView(View):
#     def get(self,request):
#         form=LoginForm()
#         return render(request,"login.html",{"form":form})
    

class LoginView(FormView):
    template_name='login.html'
    form_class=LoginForm
    def post(self,request):
        form_data=LoginForm(data=request.POST)
        if form_data.is_valid():
            uname=form_data.cleaned_data.get('username')
            pswd=form_data.cleaned_data.get('password')
            user=authenticate(request,username=uname,password=pswd)
            print(user)
            if user:
                login(request,user)
                messages.success(request,"Login successful!!")
                return redirect('home')
            else:
                messages.error(request,"Login Failed.Invalid Username/Password")
                return redirect('log')
        else:
            return render(request,"login.html",{"form":form_data})
        
    
# class RegView(View):
#     def get(self,request):
#         form=RegForm()
#         return render(request,"reg.html",{"form":form})
#     def post(self,request):
#         from_data=RegForm(data=request.POST)
#         if from_data.is_valid():
#             from_data.save()
#             messages.success(request,"User Registration successfull!!")
#             return redirect('log')
#         else:
#             messages.error(request,"Registration Failed!!")
#             return render(request,"reg.html",{"form":from_data})
        

class RegView(CreateView):
    form_class=RegForm
    template_name="reg.html"
    success_url=reverse_lazy('log')


class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('log')
