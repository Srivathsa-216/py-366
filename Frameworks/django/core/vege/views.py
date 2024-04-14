from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url = "/login/")
def reciepe(request):

    if request.method == "POST":
            
        data = request.POST
        print(data)

        reciepe_name = data.get("reciepe_name")
        print("Reciepe Name ::",reciepe_name)

        reciepe_description = data.get("reciepe_description")
        print("Reciepe Description ::",reciepe_description)

        reciepe_image = request.FILES.get('reciepe_image')
        print("Reciepe Image :: ",reciepe_image)

        Reciepe.objects.create(
            reciepe_name = reciepe_name,
            reciepe_description = reciepe_description,
            reciepe_image = reciepe_image
        )

        return redirect('/reciepe/')
    
    queryset = Reciepe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(reciepe_name__icontains = request.GET.get('search'))

    context = {'reciepes': queryset}

    return render(request, "reciepes.html", context)

@login_required(login_url = "/login/")
def delete_reciepe(request, id):

    queryset = Reciepe.objects.get(id = id)
    queryset.delete()
    return redirect('/reciepe/')

@login_required(login_url = "/login/")
def update_reciepe(request, id):
    queryset = Reciepe.objects.get(id = id)
    context = {'reciepe': queryset}

    if request.method == "POST":
        data = request.POST

        reciepe_name = data.get("reciepe_name")
        reciepe_description = data.get("reciepe_description")
        reciepe_image = request.FILES.get('reciepe_image')

        queryset.reciepe_name = reciepe_name
        queryset.reciepe_description = reciepe_description
        
        if reciepe_image:
            queryset.reciepe_image = reciepe_image

        queryset.save()
        return redirect('/reciepe/')

    return render(request, 'update_reciepe.html', context)

def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login/')
        
        else:
            login(request, user)
            return redirect('/reciepe/')


    return render(request, 'login.html')

def register(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, "Username already exists, Please register again with new username")
            return redirect('/register/')


        user = User.objects.create(
            first_name =first_name,
            last_name = last_name,
            username = username

        )

        user.set_password(password)

        user.save()
        messages.info(request, "Account Created successfuly")

        return redirect('/register/')

    return render(request, 'register.html')

def logout_page(request):

    logout(request)
    return redirect('/login/')