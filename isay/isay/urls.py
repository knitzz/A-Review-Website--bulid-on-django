"""isay URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from profiles.views import RegisterView
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from profiles.views import UserLoginView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/$',RegisterView.as_view(),name='register'),
    url(r'^$',TemplateView.as_view(template_name='index.html'),name='index'),
    url(r'^',include('profiles.urls',namespace='profiles')),
    url(r'^items/',include('items.urls',namespace='items')),

    url(r'^login/$',UserLoginView.as_view(),name='login'),
    url(r'^login/(?P<slug>[a-zA-Z]+)/$',UserLoginView.as_view(),name='login'),
    url(r'^logout/$',LogoutView.as_view(),name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)