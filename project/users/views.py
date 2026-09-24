from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from . forms import User_Registration_Form, Login_Form
from .models import User_Registration_Table
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'base.html')

def register_view(request):
    if request.method == 'POST':
        form = User_Registration_Form(request.POST)

        if form.is_valid():

            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            cellphone = form.cleaned_data['cellphone']
            study_path = form.cleaned_data['study_path']
            level = form.cleaned_data['level']
            github = form.cleaned_data['github_url']
            password = form.cleaned_data['password1']

            if User.objects.filter(username=email).exists():
                messages.error(request,'Email already exist!')
                return render(request, 'register.html', {'form': form})
            else :
                user = User.objects.create_user(
                    username = email,
                    password = password,
                )
                
                register_user = User_Registration_Table.objects.create(
                    user = user,
                    full_name = full_name,
                    cellphone = cellphone,
                    study_path = study_path,
                    level = level,
                    github_url = github,
                )

                context = {
                    'full_name': register_user.full_name,
                    'email': user.username,
                    'active_status': register_user.active_status
                    }
                return render(request,'pending_approval.html', {'user': context})
    else :
        form = User_Registration_Form()
    return render(request,'register.html', {'form': form})                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     

         
def login_view(request):
    if request.method == 'POST':

        form = Login_Form(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
 
            user = authenticate(request, username=email,password=password)

            if user is not None:

                user_info = User.objects.get(username=email)
                user_get = User_Registration_Table.objects.get(user=user_info.pk)

                full_name = user_get.full_name
                active_status = user_get.active_status

                if active_status == 'Approved' :
                    login(request, user)
                    return render(request, 'participant_dashboard.html', {'request':request})
        
                else: 
                    context = {
                        'full_name':full_name,
                        'email': email,
                        'active_status':active_status,
                        }
                    return render(request, 'pending_approval.html',{'user':context })
            else :
                messages.error(request,"Account doesn't exist!")
                return render(request, 'login.html', {'form': form})

    else :
        form = Login_Form()
    return render(request, 'login.html', {'form': form})



def logout_view(requst):
    pass
