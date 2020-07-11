from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate


# Create your views here.
def login_view(request):
    msg = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            msg = 'User not exist..!'

        else:
            login(request, user)
            # return redirect('')

    return render(request, 'login.html', {'msg': msg})