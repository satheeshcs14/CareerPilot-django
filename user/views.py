from django.shortcuts import render


# user/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']  # company or employee

        user = User.objects.create_user(username=username, password=password)

        group = Group.objects.get(name=role.capitalize())
        user.groups.add(group)

        return redirect('login')

    return render(request, 'register.html')