"""rindus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import logout

from client_management import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.main),
    url(r'^main', views.main),
    url(r'^add', views.add),
    url(r'^create', views.create),
    url(r'^edit/(?P<client_id>[0-9]+)', views.edit),
    url(r'^update/(?P<client_id>[0-9]+)', views.update),
    url(r'^delete/(?P<client_id>[0-9]+)', views.delete),
    url('', include('social_django.urls', namespace='social')),
    url('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
]
