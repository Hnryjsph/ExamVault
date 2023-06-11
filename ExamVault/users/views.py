from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
	return render(request, 'dashboard.html', {})


def register(request):
    if request.method == 'POST':
        
        data = {
        'csrfmiddlewaretoken': request.POST['csrfmiddlewaretoken'],
        'username': request.POST['username'],
        'phone_number': request.POST['phone number'] , 
        'password1': request.POST['password'], 
        'password2': request.POST['password confirmation'],
        }

        form = CustomUserCreationForm(data)
     
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        
        data = {
    	'csrfmiddlewaretoken': request.POST['csrfmiddlewaretoken'],
    	'username': request.POST['username'],
    	'password': request.POST['password'],
    	}
        
        form = LoginForm(data)
        if not(form.is_valid()):
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                return redirect('/')  # Redirect to the desired page after successful login
            else:
                messages.error(request, 'Invalid email or password.')
               
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})


@login_required
def logout_view(request):
	logout(request)

	return redirect("/login/")

@login_required
def faq_view(request):
	return render(request, 'faq.html', {})

@login_required
def profile_view(request):
	return render(request, 'profile.html', {})

@login_required
def contact_view(request):
	return render(request, 'contact.html', {})

@login_required
def dashboard_view(request):
	return render(request, 'dashboard.html', {})
