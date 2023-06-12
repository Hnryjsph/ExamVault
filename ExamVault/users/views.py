from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, UpdateUserForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.contrib.auth.hashers import make_password
from django.urls import reverse_lazy


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
    user_update_form = UpdateUserForm()
    if request.method == "POST":
        if 'username' in request.POST:
            username = request.POST['username']
            first_name = request.POST['first name']
            last_name = request.POST['last name']
            gender = request.POST['gender']
            phone_number = request.POST['phone number']
            course = request.POST['course']
            email = request.POST['email']
            university = request.POST['university']
            country = request.POST['country']

            user = CustomUser.objects.get(pk = request.user.id)
            user.username = username
            user.first_name = first_name
            user.last_name = last_name
            user.gender = gender
            user.phone_number = phone_number
            user.course = course
            user.email = email
            user.university = university
            user.country = country
            user.save()
            return redirect('/profile/')

        elif "password" in request.POST:
            password = request.POST['password']
            newpassword = request.POST['newpassword']
            renewpassword = request.POST['renewpassword']

            user = CustomUser.objects.get(pk = request.user.id)
            user_auth = authenticate(username = user.username, password = password)
            if user_auth:
                if newpassword == renewpassword:
                    user.set_password(renewpassword)
                    user.save()
                    return redirect('/login/')
                else:
                    print("Passwords not the Same ")
            else:
                print("Incorrect Password")




    else:
        user_update_form = UpdateUserForm()
   
    context = {
        'user_update_form': user_update_form,
    }
    return render(request, 'profile.html', context)

@login_required
def contact_view(request):
	return render(request, 'contact.html', {})

@login_required
def dashboard_view(request):
	return render(request, 'dashboard.html', {})
