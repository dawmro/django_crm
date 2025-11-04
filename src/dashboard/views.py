from django.conf import settings
from django.shortcuts import redirect, render
import os
from pathlib import Path


TEMPLATES_DIR = settings.TEMPLATES_DIR
print("TEMPLATES_DIR", TEMPLATES_DIR, TEMPLATES_DIR.exists())
dashboard_html = Path(os.path.join(TEMPLATES_DIR, "dashboard.html"))
print("dashboard_html", dashboard_html, dashboard_html.exists())


def dashboard_webpage(request, *args, **kwargs):
    print(request.user, request.user.is_authenticated)
    if not request.user.is_authenticated:
        return redirect("/auth/google/login")
    my_value = str(request.user)
    template_context = {"my_value": my_value}
    return render(
        request=request, template_name="dashboard.html", context=template_context
    )
    # dashboard_html = Path(os.path.join(TEMPLATES_DIR, "dashboard.html"))
    # if not dashboard_html.exists():
    #     return HttpResponse("Not Found", status=404)
    # dashboard_html_val = dashboard_html.read_text()
    # _html = dashboard_html_val.format(my_value=str(request.user))
    # return HttpResponse(_html)
