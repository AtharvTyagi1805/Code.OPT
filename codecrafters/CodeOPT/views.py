from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import SignUpForm, LoginForm
from conversion import *
import os 
from django.conf import settings


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('login')  
        else:
            messages.error(request, "Registration failed. Please check the form fields and try again.")
            print(form.errors)  
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect('home')  
            else:
                messages.error(request, "Login failed. Incorrect username or password.")
                print("User authentication failed.")  
        else:
            messages.error(request, "Login failed. Please check the form fields and try again.")
            print(form.errors)  
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def expertIMP(request):
    d = {}
    try:
        if request.method == "POST":
            n1 = request.POST.get('takingcode')
            if n1:
                input_file_path = os.path.join(settings.BASE_DIR, "codecrafters", "data_extract.txt")
                output_file_path = os.path.join(settings.BASE_DIR, "codecrafters", "data_converted.txt")

                
                with open(input_file_path, 'w') as f:
                    f.write(n1)
                    print(f"Written to {input_file_path}: {n1}")

                x, _ = taking_content()  
                transfering_content(x)  

                # Read the processed output
                with open(output_file_path, 'r') as f:
                    output = f.read()
                    print(f"Read from {output_file_path}: {output}")
                    d = {'n1': n1, 'output': output}
    except Exception as e:
        print(f"Error: {e}")
    return render(request, "index.html", d)


@login_required
def aboutUS(request):
    return render(request, "about-us.html")

@login_required
def studyMAT(request):
    return render(request, "study-material.html")
