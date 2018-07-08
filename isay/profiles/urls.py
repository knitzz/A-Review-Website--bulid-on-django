from profiles.views import UserLoginView
from django.views.generic import TemplateView
from django.conf.urls import url,include
from .views import ProfileDetailView,followtoggle,homeview,search
urlpatterns = [
    url(r'^home/$', homeview,name='home'),
    url(r'^profile/(?P<username>[a-zA-Z0-9]+)$', ProfileDetailView.as_view(),name='profile'),
    url(r'^ajax/followtoggle/$', followtoggle,name='followtoggle'),
    url(r'^profile/search/', search,name='search'),

    ]