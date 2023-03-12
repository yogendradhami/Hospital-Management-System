from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import login, logout
from django.contrib import messages


# Create your views here.
def Dashboard(request):
    return render(request,'authentication/dashboard.html')

class LogoutPage(View):
    def get(self, request):
        logout(request)
        messages.success(request, "You're Logged Out !!")
        return redirect('user_login')
    
class LoginPage(View):
    def get(self, request):
        return render(request, 'authentication/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        check = request.POST['check']

        user = auth.authenticate(request, username= username, password= password,check=check)

        if user:
            login(request, user)
            messages.success(request, 'Login successfully')
            return redirect('logintemp')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('user_login')

    

class RegisterPage(View):
    def get(self,  request):
        return render(request,'authentication/register.html')
    
    def post(self, request):
        first_name= request.POST['first_name']
        last_name = request.POST['last_name']
        email= request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        try:
            # user validation
            user = User.objects.get(username=username)
            if user:
                messages.error(request, 'Username already exists. Try with new one!')
                return redirect('user_registration')
        
        except:
            date = User.objects.create_user(first_name= first_name, last_name= last_name, email=email, username=username,password=password)

            messages.success(request, 'Account has been created successfully!')
            return redirect('user_login')

        