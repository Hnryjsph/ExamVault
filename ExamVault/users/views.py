from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, UpdateUserForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Feedback, FrequentlyAskedQuestion
from django.contrib.auth.hashers import make_password
from django.urls import reverse_lazy
from questions.models import Collection, Question
from .models import TermsAndConditions

# A view for the landing page
@login_required
def home(request):

    return render(request, 'dashboard.html', {})


# A view that helps to register users 
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
            return redirect('/login/')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form': form})



# A view that helps users to login
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

                return redirect('/dashboard/')  # Redirect to the desired page after successful login
            else:
                messages.error(request, 'Invalid email or password.')
               
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})


# A view that is routed to for logout functionality
@login_required
def logout_view(request):
	logout(request)

	return redirect("/login/")


# A view that returns faqs
@login_required
def faq_view(request):
    faqs = FrequentlyAskedQuestion.objects.all()
    context = {'faqs':faqs}
    return render(request, 'faq.html', context)


# A view that returns profile and enables editing
@login_required
def profile_view(request):
    user_update_form = UpdateUserForm()
    user = CustomUser.objects.get(pk = request.user.id)
    if request.method == "POST":
        if 'username' in request.POST:
            print(request.POST)
            user = CustomUser.objects.get(pk = request.user.id)
            try:
                image = request.FILES['image']
            except Exception as e:
                image = user.image
                
            username = request.POST['username']
            first_name = request.POST['first name']
            last_name = request.POST['last name']
            gender = request.POST['gender']
            phone_number = request.POST['phone number']
            course = request.POST['course']
            email = request.POST['email']
            university = request.POST['university']
            country = request.POST['country']


            
            user.username = username
            user.first_name = first_name
            user.last_name = last_name
            user.gender = gender
            user.phone_number = phone_number
            user.course = course
            user.email = email
            user.university = university
            user.country = country
            user.image = image
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
        'person':user,
    }
    return render(request, 'profile.html', context)


# A view that returns contact/ feedback view 
@login_required
def contact_view(request):
    """ Feedback """
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        user = request.user

        feedback = Feedback()
        feedback.user = user 
        feedback.subject = subject
        feedback.message = message
        feedback.save()

        return redirect("/contact/")

    return render(request, 'contact.html', {})

# A view that returns the dashboard view 
@login_required
def dashboard_view(request):

    collection_length = len(Collection.objects.all())

    questions_length = len(Question.objects.all())
    questions_rec = Question.objects.all()[:10]

    context = {
    "collection_length":collection_length,
    "questions_length": questions_length,
    "questions_rec":questions_rec
    }
    return render(request, 'dashboard.html', context)

# A views that routes you to the terms and conditions
def terms(request):
    terms = TermsAndConditions.objects.all()
    context = {'terms':terms}

    return render(request, 'terms.html', context)