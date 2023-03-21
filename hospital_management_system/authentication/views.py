# Create your views here.
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import login, logout
from django.contrib import messages
from django.core.mail import send_mail
from .helpers import send_forget_password_mail
import uuid
from .models import Profile


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
            return redirect('home')
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
            data = User.objects.create_user(first_name= first_name, last_name= last_name, email=email, username=username,password=password)

            messages.success(request, 'Account has been created successfully!')
            send_mail(
                'Account Creation |  HMS', #subject
                'Your account has been created! \n Welcome \n' +
                data.username, #message
                'yogendradhami631@gmail.com', # sender
                [data.email] #reciever
            )
            return redirect('user_login')
        

def ChangePassword(request,token):
    context={}
    try:
        profile_obj =Profile.objects.filter(forget_password_token =token).first()

        print(profile_obj)


    except Exception as e:
        print(e)
    return render(request, 'authentication/change_password.html')

def forgetPassword(request):
    try:
        if request.method == 'POST':
            username=request.POST.get('username')

            if not User.objects.filter(username=username).first():
                messages.success(request, 'No user found with this username.')
                return redirect('forgot-password')
            
            user_obj= User.objects.get(username=username)
            token =str(uuid.uuid4())
            profile_obj = Profile.objects.get(user=user_obj)
            profile_obj.forgot_password_token=token
            
            send_forget_password_mail(user_obj, token)
            messages.success(request, 'An email is sent.')
            return redirect('forgot-password')


    except Exception as e:
        print(e)
    return render(request, 'authentication/forgot_password.html')

        