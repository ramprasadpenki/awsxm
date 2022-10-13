"""sdpproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('login/', views.login.as_view(),name='login'),
    path('signup/', views.signup.as_view(),name='signup'),
    path('request/', views.request,name='request'),
    path('logout/', views.log,name='logout'),
    path('find/', views.find,name='find'),
    path('donate/', views.don,name='donate'),
    path('view_request/', views.view_request, name='view_request'),
    path('admin_user/', views.admin_signup, name='admin_user'),
    path('adminview/', views.adminview, name='adminview'),
    path('viewdonar/', views.viewdonar, name='viewdonar'),
    path('viewbloodreq/', views.viewreq, name='viewreq'),
]
