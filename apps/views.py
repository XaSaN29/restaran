from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views.generic import TemplateView, ListView, FormView, CreateView, View, DetailView
from httpx import post, get
from .form import UserRegisterForm, UserLoginForm
from .models import Product, User, Category, Order

TELEGRAM_BOT_TOKEN = '7247047677:AAEO9mm9O6HCZOPEDt6EeBGFS_n-RF-QOyo'


class IndexViewFast(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = "product"

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(category__name="Fasfood")
        return qs

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context["categories"] = Category.objects.all()
        return context


class OrderView(ListView):
    template_name = 'order.html'
    model = Order


class IndexViewMilliy(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = "product"

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(category__name="Mili taomlar")
        return qs

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context["categories"] = Category.objects.all()
        return context


class IndexViewPizza(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = "product"

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(category__name="Pizza")
        return qs

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context["categories"] = Category.objects.all()
        return context


class AboutView(TemplateView):
    template_name = 'about.html'


class ServiceView(TemplateView):
    template_name = 'service.html'


class BookingView(TemplateView):
    template_name = 'booking.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class MenuView(ListView):
    template_name = 'menu.html'
    model = Product
    context_object_name = "product"


class TeamView(TemplateView):
    template_name = 'team.html'


class TestimonialView(TemplateView):
    template_name = 'testimonial.html'


class LoginView(FormView):
    form_class = UserLoginForm
    template_name = 'login.html'
    success_url = '/'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = User.objects.filter(username=username).first()
        if user is not None and user.check_password(password):
            login(self.request, user)
            return redirect('/')

        else:
            return redirect('register')

        return super().form_valid(form)


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = '/'


class LogoutView(View):
    def get(self, request):
        logout(self.request)
        return redirect('index')


class WishlistView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'wishlist.html'
    context_object_name = 'wishlist'


def send_message(chat_id, message):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': message
    }
    response = get(url, params=params)
    print(response.text, response.status_code)

def send_msg_bot(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        text = f'''
Name: {name}
Email: {email}
Subject: {subject}
Message: {message}
        '''
        send_message(867549831, text)

        return render(request, 'contact.html')

