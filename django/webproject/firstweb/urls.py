from django.contrib import admin
from django.urls import path

from website.views import mainpage, description,photos,login,signin
from accounts.views import login_view
urlpatterns = [
    path('',views.index)
]

urlpatterns = [

    path('',home,name='home'),

    path(r'^description/$', views.description),
    path(r'^photos/$', views.photos),
    path(r'^login/$', views.login),
    path(r'^signin/$', views.signin),
    path('accounts/login/',login_view),
]