from django.shortcuts import render
from django.http import HttpResponse
from home.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return HttpResponse("This is home Page!!")
def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'home/registration.html', {'registered':registered, 'user_form':user_form, 'profile_form':profile_form})
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request.user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account is deactivated!!")
        else:
            return HttpResponse("Please use correct ID and PASSWORD!!")