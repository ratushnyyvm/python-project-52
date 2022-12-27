from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):

    template_name = "index.html"


class UserLoginView(SuccessMessageMixin, LoginView):

    template_name = 'login.html'
    next_page = 'home'
    success_message = 'Вы залогинились!'


class UserLogoutView(SuccessMessageMixin, LogoutView):

    next_page = 'home'

    def dispatch(self, request, *args, **kwargs):
        messages.add_message(self.request, messages.INFO, 'Вы разлогинились!')
        return super().dispatch(request, *args, **kwargs)
