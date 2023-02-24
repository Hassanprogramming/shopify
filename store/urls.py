from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('Registration/', views.Registration, name="registration"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('search/', views.Search, name="search"),

    path('shop/', views.shop, name="shop"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('about/', views.about, name="about us"),
    path('<int:pid>/', views.post, name="post"),

    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
]
