from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.db.models import Q
from .models import Dish
from .forms import DishForm
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'WebApp/signup.html', {'form': form})

@login_required
def my_recipe(request):
    dishs = Dish.objects.all()
    return render(request, 'WebApp/my_recipe.html', {'dishs': dishs})

def recipe_list(request):
    dishs = Dish.objects.all()
    return render(request, 'WebApp/recipe_list.html', {'dishs': dishs})

def search(request):
    query = request.GET.get('q')
    dishs = Dish.objects.filter(Q(title__contains=query) | Q(ingredients__contains = query))
    return render(request,'WebApp/recipe_list.html', {'dishs':dishs})

def dish_detail(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    return render(request, 'WebApp/dish_detail.html', {'dish':dish})

@login_required
def dashboardView(request):
    return render(request,'WebApp/dashboard.html')

@login_required
def dish_edit(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    if request.method == "POST":
        form = DishForm(request.POST, instance=dish)
        if form.is_valid():
            dish = form.save(commit=False)
            dish.user_id = request.user
            dish.last_update = timezone.now()
            dish.save()
            return redirect('dish_detail', pk=dish.pk)
    else:
        form = DishForm(instance=dish)
    return render(request, 'WebApp/dish_edit.html', {'form': form})

@login_required
def new_dish(request):
    if request.method == "POST":
        form = DishForm(request.POST)
        if form.is_valid():
            dish = form.save(commit=False)
            dish.user_id = request.user
            dish.last_update = timezone.now()
            dish.save()
            return redirect('dish_detail', pk=dish.pk)
    else:
        form = DishForm()
    return render(request, 'WebApp/dish_edit.html', {'form': form})