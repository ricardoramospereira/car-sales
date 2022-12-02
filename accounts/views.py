from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Você agora está logado')
            return redirect('dashboard')
        else:
            messages.error(request, 'Dados do login inválido')
            return redirect('login')
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        ################ confirm register #########################
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Usuário já existe')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email já existe')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
                    auth.login(request, user)
                    messages.success(request, 'Você agora está logado')
                    return redirect('dashboard')
                    user.save()
                    messages.success(request, 'Registro salvo com sucesso')
                    return redirect('login')
        else:
            messages.error(request, 'Senha incorreta')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')
        

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Você deslogou na sua conta')
        return redirect('index')
    return redirect('index')
