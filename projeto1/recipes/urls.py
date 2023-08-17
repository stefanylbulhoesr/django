from django.urls import path

from . import views #o ponto suvstitui o nome da pasta atual



urlpatterns = [
    path('', views.home, name="recipes-home"), #/home raiz
    path('recipes/category/<int:category_id>/', views.category, name="recipes-category"),
    path('recipes/<int:id>/', views.recipe, name="recipes-recipe"),
    

]
