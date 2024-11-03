from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from mixins.search_mixin import SearchMixin
from user.forms import RegistrationForm


class RegistrationView(SearchMixin, CreateView):
    form_class = RegistrationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("store:index")

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
            return redirect(self.success_url)
        else:
            return super().form_valid(form)


class Login(SearchMixin, LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        return super().get_success_url()

    def get_redirect_url(self):
        nxt = self.request.POST.get("next")
        if nxt == "/order/add_to_cart/":
            redirect_to = '/accounts/login/'
            return redirect_to
        return super().get_redirect_url()
