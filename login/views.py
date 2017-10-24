from django.shortcuts import render
from django.views.generic import TemplateView

from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from login.forms import LoginForm

# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'

    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class LoginView(TemplateView):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')
        else:
            if request.session.get("login"):
                return HttpResponseRedirect('/')
            return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')
        else:
            mensaje = ""
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return HttpResponseRedirect('/')
                    else:
                        mensaje = "Tu usuario esta inactivo"
                else:
                    mensaje = "Nombre y/o password incorrectos"

            ctx = {'mensaje': mensaje}
            return render(request, self.template_name, ctx)

class AccountView(TemplateView):
    template_name = 'cuenta.html'

    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, *args, **kwargs):

        mensaje = ""
        
        context = {
                    'mensaje': mensaje    
                    }
        return render(request,self.template_name, context)


class LogoutView(TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect('/')
