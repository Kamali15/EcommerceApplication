
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",Home,name="home"),
    path("about",About,name="about"),
    path("login",login_user,name="login"),
    path("logout",logout_user,name="logout"),
    path("portfolio",Portfolio,name="portfolio"),
    path("register",register_user,name="register"),
    path("product/<int:pk>", Product_detail ,name = "product_detail"),
    path("category/<str:foo>",category, name = "category"),
    
]
