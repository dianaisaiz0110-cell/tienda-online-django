from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import ProductoForm
from .models import Producto


def home(request):
    return render(request, 'tienda/home.html')


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'tienda/registro.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'tienda/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/producto_list.html', {'productos': productos})


@login_required
def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm()

    return render(request, 'tienda/producto_form.html', {'form': form})


@login_required
def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'tienda/producto_form.html', {'form': form})


@login_required
def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == 'POST':
        producto.delete()
        return redirect('producto_list')

    return render(request, 'tienda/producto_confirm_delete.html', {'producto': producto})