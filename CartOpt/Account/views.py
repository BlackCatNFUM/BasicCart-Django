from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import UserChangeFormMod
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginHandler(View):
    def get(self, request):
        if request.user.is_anonymous:
            return render(request, "Account/login.html")
        else:
            messages.error(request, "You Are Already Logged In")
            return redirect('/')
    def post(self, request):
        if request.user.is_anonymous:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if username and password:
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logined Successfully!")
                    return redirect("/")
                else:
                    messages.error(request, "User Not Founded. Try Again")
                    return redirect("Account:login")
        else:
            messages.error(request, "You Are Already Logged In")
            return redirect('/')
        
        
class RegisterHandler(View):

    def get(self, request):
        form = UserCreationForm
        return render(request, "Account/register.html", {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully, Please Login")
            return redirect("Account:login")
        
        return render(request, "Account/register.html", {'form': form})


class ChangeAccountInfo(LoginRequiredMixin, View):
    login_url = 'Account:login'
    def get(self, request):
        form = UserChangeFormMod(instance=request.user)
        return render(request, "Account/change.html", {'form': form})

    def post(self, request):
        form = UserChangeFormMod(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Edited Successfully")
            return redirect('Account:change')

def logout_handler(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logout Successfully!")
        return redirect("/")
    else:
        messages.error(request, "You Are Already logged out")
        return redirect("/")