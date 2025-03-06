from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .form import ItemForm
# Create your views here.

def index(req):
    items = User.objects.all()
    return render(req, 'user/user.html', {'items': items})

def create_user(req):
    if req.method == 'POST':
        form = ItemForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ItemForm()

    return render(req, 'user/user_form.html', {'form': form})

def update_user(req, pk):
    user = get_object_or_404(User, pk=pk)
    if req.method == 'POST':
        form = ItemForm(req.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ItemForm(instance=user)
    return render(req, 'user/user_form.html', {'form': form})

def delete_user(req, pk):
    user = get_object_or_404(User, pk=pk)
    if req.method == 'POST':
        user.delete()
        return redirect('index')
    return render(req, 'user/confirm_delete.html', {'item': user})