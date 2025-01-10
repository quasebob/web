from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Client

# Список пользователей
def user_list(request):
    clients = Client.objects.all()  # Получаем всех пользователей
    return render(request, 'users/user_list.html', {'clients': clients})

# Регистрация
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile', username=form.cleaned_data['username'])
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})

# Профиль пользователя
def profile(request, username):
    client = Client.objects.get(username=username)
    return render(request, 'users/profile.html', {'client': client})
