"""trainsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from trainsite import settings #settings - module
from women.views import *
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha',include('captcha.urls')),
    path('', include('women.urls')), #delete pref women- and all routes - from domen name

]
if settings.DEBUG: #in checking, not it in fight
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #add rout in che
    #for static data, graphic files add 1)prefix MEDIA, 2) root folder, where located files

handler404 = pageNotFound #create handler
