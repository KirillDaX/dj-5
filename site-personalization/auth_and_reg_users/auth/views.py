from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from auth.forms import SignupForm, LoginForm


def home(request):
    return render(
        request,
        'home.html'
    )


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
        user_name = form.cleaned_data.get('username')
        user_password = form.cleaned_data.get('password')
        user = authenticate(username=user_name, password=user_password)
        login(request, user)
        return redirect('home')
    else:
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})


def login_view(request):
    user_value = ''
    password_value = ''
    form = LoginForm(request.POST or None)
    if form.is_valid():
        user_value = form.cleaned_data.get("username")
        password_value = form.cleaned_data.get("password")

        user = authenticate(username=user_value, password=password_value)
        if user is not None:
            login(request, user)
            context = {'form': form,
                       'error': 'Успешный вход!'}

            return render(request, 'login.html', context)
        else:
            context = {'form': form,
                       'error': 'Не верное сочетание Имени пользователя и Пароля'}

            return render(request, 'login.html', context)

    else:
        context = {'form': form}
        return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return render(
        request,
        'logout.html'
    )
