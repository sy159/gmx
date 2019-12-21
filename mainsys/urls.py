import os
from mainsys.settings import APP_ROOT, APPS_CANNOT_INTSALL
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]

# 根据apps里的目录进行动态添加url
for ap in os.listdir(APP_ROOT):
    if ap not in APPS_CANNOT_INTSALL and os.path.isdir(os.path.join(APP_ROOT, ap)) and \
            os.path.exists(os.path.join(os.path.join(APP_ROOT, ap), "__init__.py")) and \
            os.path.exists(os.path.join(os.path.join(APP_ROOT, ap), "urls.py")):
        urlpatterns.append(path(ap + "/", include(ap + ".urls")))
