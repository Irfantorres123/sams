from django.shortcuts import render
from django.views import View

# Create your views here.


class LoginView(View):
    template_name = 'user/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)