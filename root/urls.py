"""
URL configuration for root project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from tkinter import Menu

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from apps.views import (
    IndexViewFast, AboutView, ServiceView,
    BookingView, ContactView, MenuView,
    TeamView, TestimonialView, LoginView,
    RegisterView, LogoutView, WishlistView,
    IndexViewMilliy, OrderView,
    IndexViewPizza, send_msg_bot
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexViewFast.as_view(), name='index'),
    path('milly/', IndexViewMilliy.as_view(), name='indexmilliy'),
    path('pizza/', IndexViewPizza.as_view(), name='indexpizza'),

    path('about/', AboutView.as_view(), name='about'),

    path('order/', OrderView.as_view(), name='order'),

    path('service/', ServiceView.as_view(), name='service'),

    path('booking/', BookingView.as_view(), name='booking'),

    path('contact/', ContactView.as_view(), name='contact'),

    path('menu/', MenuView.as_view(), name='menu'),

    path('team/', TeamView.as_view(), name='team'),

    path('testimonial/', TestimonialView.as_view(), name='testimonial'),

    path('login/', LoginView.as_view(), name='login'),

    path('register/', RegisterView.as_view(), name='register'),

    path('logout/', LogoutView.as_view(), name='logout'),

    path('wishlist/', WishlistView.as_view(), name='wishlist'),

    path('send_msg_bot/', send_msg_bot, name='send_msg_bot'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
