
from django.shortcuts import render , get_object_or_404,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.views.generic import DetailView,View,CreateView
from .forms import RegisterForm
from .models import Profile
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from .models import followinguser_item
from  items.models import ItemModel
from django.contrib.postgres.search import SearchVector
User=get_user_model()
# Create your views here.


def search(request):
	query=request.POST.get('search')
	item_list=ItemModel.objects.filter( title__icontains=query)
	return render(request,"profiles/search.html",context={'item_list':item_list})
def homeview(request):
	if request.user.is_authenticated() :
		item_list=followinguser_item(request.user)
		print(item_list)
		return render(request,"profiles/home.html",context={'item_list':item_list})
	else:
		return redirect("/login/")





class RegisterView(CreateView):
	form_class=RegisterForm
	template_name="registration/register.html"
	success_url="/login/regsuccess/"

	def dispatch(self,  *args, **kwargs):
		if self.request.user.is_authenticated():
			return redirect("/home")
		return super(RegisterView,self).dispatch(*args,**kwargs)

	def get_context_data(self, *args,**kwargs):
	    context = super(RegisterView, self).get_context_data(**kwargs)
	    # a=context['form'].username;
	    # print(a.as_p()[3])
	    return context

class UserLoginView(LoginView):
# redirect_field_name='loginsuccess' BY default 'NEXT'

	def dispatch(self,  *args, **kwargs):
		if self.request.user.is_authenticated():
			return redirect("/home")
		return super(UserLoginView,self).dispatch(*args,**kwargs)

	def get_context_data(self,*args,**kwargs):
		context=super(UserLoginView,self).get_context_data(*args,**kwargs)
		if(self.kwargs.get('slug')):
			context['reg']=True
		return context



class ProfileDetailView(DetailView):
	template_name="profiles/profile.html"

	def get_object(self):
		username=self.kwargs.get("username")

		return get_object_or_404(User, username = username)


def followtoggle(request):
	
	toggle=User.objects.filter(username=request.POST.get('username'))[0]
	requesteduser=User.objects.filter(username=request.user)[0]
	if requesteduser in toggle.profile.followers.all():
		toggle.profile.followers.remove(requesteduser)
		data={'flag' : False}
	else :
		toggle.profile.followers.add(requesteduser)
		data={'flag' : True}
	return JsonResponse(data)
