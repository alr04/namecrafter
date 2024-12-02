from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import SignupForm, LoginForm

# def register(request):
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#     confirm_password = request.POST.get('password2')     
#     if password != confirm_password:
#         messages.error(request, "Passwords do not match")
#         return render(request, 'login/signup.html')

#     newUser = User(username=username)
#     newUser.set_password(password)
#     newUser.save()
#     messages.success(request, 'Registered successfully!')
#     return render(request, 'login/login.html')


# def log_in(request):
#     username = request.POST.get('username')
#     password = request.POST.get('password')

#     user = authenticate(request, username=username, password=password)

#     if user is not None:
#         login(request, user)
#         messages.success(request, "You have logged in successfully!")
#         return redirect(views.homepage) 
#     else:
#          messages.error(request, "Invalid username or password.")
#          return render(request, 'login/login.html')
 


def log_in(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard1:homepage") 
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created successfully.")
            return redirect('login:login')
    else:
        messages.error(request, "Invalid username or password.")
        form = SignupForm()
    return render(request, 'login/signup.html', {'form': form})
