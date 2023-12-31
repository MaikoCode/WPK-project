"""
URL configuration for wpkProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView

import authentication.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", authentication.views.login_page, name="login_page"),
    path("login/", authentication.views.login_page, name="login_page"),
    path("sign_up/", authentication.views.sign_up_page, name="sign_up_page"),
    path("user_home/", authentication.views.user_home, name="user_page"), 
    path("supplier_page/", authentication.views.supplier_page, name="supplier_page"),
    
    # TODO: Vue de deconnexion
      
]



# On va avoir un switch entre nos differentes applications en nous servant du mode d'url et des vues


