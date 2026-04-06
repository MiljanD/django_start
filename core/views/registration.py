from core.forms.user_registration_form import UserRegistrationForm
from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed


def show_registration_form(request):
    form = UserRegistrationForm()
    return render(request, "register_form.html", {"form": form})

def register_user(request):
    if request.method != "POST":
        return HttpResponseNotAllowed("This method is not allowed")

    registration_form = UserRegistrationForm(request.POST)
    if registration_form.is_valid():
        registration_form.save()
        return redirect("login_page")

    return redirect("register_form")





