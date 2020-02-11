from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.recipe_list, name='home'),
    path('WebApp/search/', views.search, name='search'),
    path('WebApp/recipe_list/', views.recipe_list, name='home'),
    path('WebApp/login/', LoginView.as_view(), name="login_url"),
    path('WebApp/dashboard/', views.dashboardView, name='dashboard'),
    path('WebApp/signup/', views.signup, name='signup'),
    path('WebApp/logout/', LogoutView.as_view(next_page='home'),name="logout"),
    path('WebApp/<int:pk>/', views.dish_detail, name='dish_detail'),
    path('WebApp/my_recipe', views.my_recipe, name='my_recipe'),
    path('WebApp/<int:pk>/edit/', views.dish_edit, name='dish_edit'),
    path('WebApp/new/', views.new_dish, name='new_dish'),
]