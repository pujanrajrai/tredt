from django.shortcuts import render,redirect
from django.contrib import auth,messages
from .models import CustomUser
from django.http import Http404
from accounts.forms import CustomUserForm
from django.contrib.auth.hashers import make_password

# Create your views here.


def     register(request):
    if request.user.is_authenticated:
        if request.user:
            return redirect('home:home')
    context={"forms":CustomUserForm()}
    if request.method=="POST":
        data=request.POST.copy()

        password1=data.get('password','')
        password2=data.get('password2','')
        
        data['password'] = make_password(password1)
        forms=CustomUserForm(data,request.FILES)

        if password1!=password2:
            context['forms']=forms
            context["errors"]="Password Didnot Match"
            return render(request,'accounts/signup.html',context)

        if forms.is_valid():
            forms.save()
            user = auth.authenticate(username=data.get('username'), password=data.get('password2'))
            if user is not None:
                auth.login(request, user)

                messages.success(request,
                             f'Congratulation You have been registered in our system.')
                return redirect('home:home')
        else:
            context['forms']=forms
    return render(request,'accounts/signup.html',context)



def login(request):
    context={}
    if request.user.is_authenticated:
        if request.user:
            return redirect('home:home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request,
                             f'Congratulation You Logged into our system.')
            return redirect('home:home')
        else:
            context['errors'] = "User name or password is incorrect"
            context['username'] = username
            return render(request, 'accounts/login.html', context)
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('home:home')


def view_profile(request,username):
    try:
        context={"profile":CustomUser.objects.get(username=username)}
        # import pdb;pdb.set_trace()
        if request.user.username == context['profile'].username or request.user.is_superuser:
            return render(request,'accounts/profile.html',context)
    except:
        pass
    raise Http404