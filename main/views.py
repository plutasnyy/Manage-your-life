from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth import views as auth_views
from  django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm


from main.forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('Homepage')
    else:
        form = SignUpForm()
    return render(request, 'registration.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

class Homepage(auth_views.LoginView):
    template_name='index.html'
