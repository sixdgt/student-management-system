from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth

# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, "authentication/login.html")
    
    def post(self, request):
        req_username = request.POST.get('username')
        req_password = request.POST.get('password')

        if req_username and req_password:
            user = auth.authenticate(username=req_username, password=req_password)

            if user:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, 'Welcome, ' + user.username + "You're logged in!!")
                    return redirect("students")
                messages.error(request, 'Account is not active')
                return redirect('login')
            messages.error(request, 'Invalid credentials, try again')
            return redirect('login')
    

class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        messages.success(request, "You're logged out")
        return redirect("login")


class RegisterView(View):
    def get(self, request):
        return render(request, "authentication/register.html")

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        context = {'fieldValues': request.POST}

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 6:
                    messages.error(request, "Password too short", context)
                    return render(request, 'authentication/register.html')
                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.is_active = True
                user.save()
                messages.success(request, 'Account created successfully!!')
        return render(request, "authentication/register.html")