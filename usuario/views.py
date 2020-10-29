from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def cadastro(request):
    if request.method == 'POST':
        usua = request.POST['user']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if not usua.strip():
            print ('User em branco nao pode')
            return redirect('cadastro')

        if not fname.strip():
            print ('Fnameem branco nao pode')
            return redirect('cadastro')

        if not lname.strip():
            print ('Lname em branco nao pode')
            return redirect('cadastro')
        
        if not email.strip():
            print ('Email em branco nao pode')
            return redirect('cadastro')

        if not usua.strip():
            print ('User em branco nao pode')
            return redirect('cadastro')

        if senha != senha2:
            print('senha não são iguais')
            return redirect('cadastro')
        
        if User.objects.filter(email=email).exists():
            print('User ja cadastrado')
            return redirect('cadastro')
        
        user = User.objects.create_user(username=usua, first_name=fname, last_name=lname, email=email, password=senha)
        user.save()
        print('Usuario cadastrado')

        print(usua, fname, lname, email, senha, senha2)
        return redirect('login')
    return render(request, "usuarios/cadastro.html")

def login (request):
    if request.method == "POST":
        email = request.POST ['email']
        senha = request.POST ['senha']
        
        if email == "" or senha == "":
            print("Campos vazios")
            return redirect ('login')

        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print("login com sucesso")
                return redirect ('dashboard')




    return render(request, "usuarios/login.html")

def logout(request):
    auth.logout(request)
    return redirect("login")

def dashboard(request):
        if request.user.is_authenticated:
            return render(request, "usuarios/dashboard.html")
        else:
            return redirect('login')