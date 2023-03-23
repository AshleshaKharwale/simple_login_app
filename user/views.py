from django.shortcuts import HttpResponse, render


def user(request):
    return render(request, 'user_login.html')


def validate(request):
    if request.method == 'POST':
        user_db = {
            'username': "ashlesha",
            'password': "zxcvbnm"
        }
        if request.POST.get('username') and request.POST.get('password'):
            username = request.POST.get('username')
            password = request.POST.get('password')
            if username == user_db['username'] and password == user_db['password']:
                return HttpResponse("Login Successful!")
            else:
                return HttpResponse("Invalid Username or password")
        else:
            return HttpResponse("Please Enter username and password")
    else:
        return HttpResponse("Get method")

