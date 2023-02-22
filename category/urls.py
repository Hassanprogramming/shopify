from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.category, name="category"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
]