from django.contrib.auth.models import User
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib import messages


class SignUpView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'registration/signup.html')

    def post(self, request, *args, **kwargs):
        form = request.POST
        username = form.get('username')
        password = form.get('password')
        confirm_password = form.get('confirm_password')
        if User.objects.filter(username=username):
            messages.add_message(request, messages.INFO, '{0} такое имя уже занято.'.format(username))
            return render(request, 'registration/signup.html')
        elif password != confirm_password:
            messages.add_message(request, messages.INFO, 'Пароли не совпадают!')
            return render(request, 'registration/signup.html')
        else:
            user = User(username=username, password=password)
            user.save()
        return redirect('login')

    
    