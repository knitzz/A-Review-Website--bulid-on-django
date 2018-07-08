from items.views import saveitem
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView
from django.conf.urls import url,include
urlpatterns = [
    url(r'^saveitem/$', saveitem,name='saveitem'),
    ] 
