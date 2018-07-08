from django.shortcuts import render
from django.shortcuts import render , get_object_or_404,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.views.generic import DetailView,View,CreateView
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from .models import ItemModel


def saveitem(request):	
	title=request.POST.get('title')
	review=request.POST.get('review')
	rating=request.POST.get('rating')
	item=ItemModel()
	item.rating=rating
	item.user=request.user
	item.title=title
	item.review=review
	if request.FILES :
		item.image=request.FILES['image']
	item.tags=request.POST.get("tags")
	item.save()
	print(request.POST.get('tags'))
	data={'true':'true'}
	return JsonResponse(data)
