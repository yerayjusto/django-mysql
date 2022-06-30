from django.urls import re_path as url
from app import views

from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns=[

    url(r'^departments$', views.departmentApi),
    url(r'^departments/([0-9]+)$', views.departmentApi),

    url(r'^employees$', views.employeeApi),
    url(r'^employees/([0-9]+)$', views.employeeApi),

    url(r'^employee/savefile', views.SaveFile)

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
