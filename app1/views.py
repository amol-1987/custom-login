from django.shortcuts import render, redirect
from app1.forms import UserAdminCreationForm


def index(req):
    d = {'inject':'Hello'}
    return render(req, 'index.html', {'inject': d})

def register(req):
    form = UserAdminCreationForm()
    if req.method == 'POST':
        form = UserAdminCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    return render(req, 'register.html', {'form': form})