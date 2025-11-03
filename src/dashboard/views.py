from django.shortcuts import redirect
from django.http import HttpResponse

# Create your views here.


def dashboard_webpage(request, *args, **kwargs):
    print(request.user, request.user.is_authenticated)
    if not request.user.is_authenticated:
        return redirect("/auth/google/login")
    return HttpResponse(f"hello {request.user}")
