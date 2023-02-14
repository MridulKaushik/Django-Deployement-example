from django.shortcuts import render
from AppFive.forms import UserForm, UserProfileinfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout

# Create your views here

def index(request):
    content = {
        "A" : "[APPLE, BANANA, FRUITS]",
        "C" : "[CITA, CITRUS, CAT]"
    }
    return render(request,"AppFive/index.html")

def other(request):
    return render(request,"AppFive/other.html")


@login_required
def special(request):
    return HttpResponse("You are logged in!!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('AppFive/index'))

def registeration(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileinfoForm(data = request.POST)

        if user_form.is_valid()and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileinfoForm()

    return render(request,"AppFive/registeration.html",{'user_form':user_form,
                                                       'profile_form':profile_form,
                                                       'registered' :registered})

def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active():
                login(request, user)
                # IF the user has logged in successfuly and he will be redirect back to homepage
                return HttpResponseRedirect(reverse('AppFive/index'))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else :
            print("InValid User tried to log in")
            print(f"Username:{username} and Password:{password}")
            print("Username:{} and Password:{}".format(username,password))
            return HttpResponse("INVALID EMAIL DETAILS SUBMITTED")
    
    else:
        return render(request, 'AppFive/login.html')

