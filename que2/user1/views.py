
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        gender = request.POST['gender']
        address= request.POST['address']
        bloodgroup = request.POST['bloodgroup']
        password = request.POST['password']

        user = User.objects.create(name=name, email=email, gender=gender, address=address, blood_group=bloodgroup, password=password)
        user.save()
        alert = True
        return render(request, 'user1/register.html', {'alert':alert})
    return render(request, 'user1/register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                # return redirect('/view_books')
                return HttpResponse('sucessfull')
            else:
                return HttpResponse('You are not an admin.')
        else:
            alert = True
            return render(request, 'user1/login.html', {'alert':alert})
    return render(request, 'user1/login.html')
    