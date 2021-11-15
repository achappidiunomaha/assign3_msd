from django.shortcuts import redirect, render
from django.views.generic import TemplateView


# class SignUpView(TemplateView):
#     template_name = 'registration/signup.html'
#

def home(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('employee:employee_home')
        elif request.user.is_client:
            return redirect('client:client_home')
    return render(request, 'ski/home.html')


def signup(request):
    return render(request, 'registration/signup.html')
