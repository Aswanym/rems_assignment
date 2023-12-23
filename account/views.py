from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import UserCreationForm
from .forms import LoginForm
from property.models import Property


def index(request):
    return render(request, 'account/index.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration completed.")
            return redirect('index')
        else:
            messages.error(request, "Registration not completed, Try again.")
            return redirect('signup')
    form = UserCreationForm()
    return render(request, 'account/signup.html', context={"form": form})

# def signup(request):
#     if request.user.is_authenticated:
#         return redirect('index')
#
#     if request.method == 'POST':
#         email = request.POST['email']
#         name = request.POST['name']
#         password = request.POST['password']
#         user = User.objects.create_user(email=email, name=name, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, "Registration completed.")
#             return redirect('index')
#         else:
#             messages.error(request, "Registration not completed, Try again.")
#             return redirect('signup')
#     return render(request, 'account/signup.html')

def login_request(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == "POST":

        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {user.name}.")
            return redirect("index")
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, "account/login.html")

    return render(request, "account/login.html")

def logout_request(request):
    if request.user.is_authenticated and request.user.is_superuser:
        logout(request)
        return redirect('admin_login')

    elif request.user.is_authenticated:
        logout (request)
        return redirect('index')

def admin_home(request):
    property_list = Property.objects.all()
    return render(request, 'account/admin_home.html', {'property_list': property_list})


def admin_login(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('admin_home')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    # Redirect to a success page after login
                    return redirect('admin_home')
                else:
                    # not admin login credentials
                    return render(request, 'account/admin_login.html', {'form': form, 'error': 'please give admin credentials'})
            else:
                # Invalid login credentials
                return render(request, 'account/admin_login.html', {'form': form, 'error': 'Invalid email or password'})
    else:
        form = LoginForm()
    return render(request, 'account/admin_login.html', {'form': form})
