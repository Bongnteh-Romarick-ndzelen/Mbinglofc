from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Profile, BlogPost, UpcomingMatches, Results
from .forms import ContactForm



# Create your views here.
@login_required(login_url="login")
def index(request):
    BlogPosts = BlogPost.objects.all()
    Matches = UpcomingMatches.objects.all()
    Result = Results.objects.all()
    
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.info(request,'Thank you!, Your message has been submitted successfully.')
        return HttpResponseRedirect("/")
    
    context = {
        'BlogPosts': BlogPosts,
        'form': form,
        'Matches': Matches,
        'Result':Result
    }
    
    return render(request, "index.html", context)


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        first_name = request.POST['first_name']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(
                    request, "Email already Exist, used a different email address"
                )
                return redirect("signup")

            if User.objects.filter(username=username).exists():
                messages.info(
                    request,
                    "Username already in used, used a different username to register",
                )
                return redirect("signup")
            if User.objects.filter(first_name=first_name).exists():
                messages.info(request, 'Phone number already exist')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password, first_name=first_name
                )
                user.save()

                # log user in and direct to settings page
                user_login = auth.authenticate(
                    username=username, password=password
                )
                auth.login(request, user_login)

                # create a Profile model for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(
                    user=user_model, id_user=user_model.id
                )
                new_profile.save()
                return redirect("login")
        else:
            messages.info(
                request,
                "Password not Matching, please make sure the two passwords are the same!",
            )
            return redirect("signup")
    else:
        return render(request, "signup.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")

        else:
            messages.info(
                request,
                "Invalid Credentials, please make sure you enter the correct information in oder to login",
            )
            return redirect("login")
    else:
        return render(request, "login.html")

@login_required(login_url="login")
def profile(request):
    return render(request, "profile.html")

@login_required(login_url="login")
def settings(request):
    user_profile = Profile.objects.get(user = request.user)
    
    if request.method == 'POST':
        if request.FILES.get('image') == None:
            profileimg = user_profile.profileimg
            bio = request.POST['bio']
            location = request.POST['location']
            
            user_profile.profileimg = profileimg
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
            
        if request.FILES.get('image') != None:
            profileimg = user_profile.profileimg
            bio = request.POST['bio']
            location = request.POST['location']
            
            user_profile.profileimg = profileimg
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
            
        return redirect('settings')
    return render(request, "settings.html",{'user_profile':user_profile})

@login_required(login_url="login")
def logout(request):
    auth.logout(request)
    return redirect("login")

