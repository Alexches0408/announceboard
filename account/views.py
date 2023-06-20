from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.urls import resolve
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

import random

from .forms import BaseRegisterForm, ConfirmPassword
from .models import OneTimeCode

def generate_code():
    random.seed()
    return str(random.randint(10000,99999))

class UsualLoginView(CreateView):
    model = User
    form_class = BaseRegisterForm

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            code = generate_code()
            OneTimeCode.objects.create(code=code, user=user)
            user_id = OneTimeCode.objects.get(code=code, user_id=user.id).user_id
            # send one time code
            mail_subject = 'Activation password for account from mmorpg announce board'
            html_content = render_to_string('account/activate.html', {
                'user': user,
                'code': code,
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMultiAlternatives(mail_subject, code,from_email='Tchesnokov.4lexander@yandex.ru', to=[to_email])
            email.attach_alternative(html_content, "text/html")
            email.send()
            return redirect(f'/account/signupcode/{user_id}/')
        else:
            form = self.form_class()
        return render(request, '/account/signup.html', {'form': form})


class LoginWithCodeView(CreateView):
    model = User
    form_class = ConfirmPassword

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.id = resolve(self.request.path_info).kwargs['pk']
        user = User.objects.get(id=self.id)
        context['user'] = user
        return context

    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            code = request.POST['code']
            user_id = request.POST['user']
            if OneTimeCode.objects.filter(code=code, user_id=user_id).exists():
                user = User.objects.get(id = user_id)
                user.is_active = True
                user.save()
                return redirect('/announces/')
            else:
                print('Ошибка одноразового кода')



