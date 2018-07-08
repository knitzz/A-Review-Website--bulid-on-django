from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.conf import settings

from items.models import ItemModel


User= settings.AUTH_USER_MODEL
temp_user=get_user_model()

class ProfileManager(models.Manager):
	pass

class Profile(models.Model):

	user=models.OneToOneField(User)
	followers=models.ManyToManyField(User,related_name='is_following',blank=True)
	# activation_key=models.CharField(max_length=120,blank=True,null=True)
	timestamp=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)

	objects=ProfileManager()

	def __str__(self):
		return self.user.username

	def count_followers(self):
		return self.followers.all().count()
		
	def count_following(self):
		return self.user.is_following.all().count()



def post_save_user_receiver(sender,instance,created,*args,**kwargs):
	if created:
		profile , is_created = Profile.objects.get_or_create(user=instance)

post_save.connect(post_save_user_receiver,sender=User)


def followinguser_item(u):
	f=u.is_following.all()
	l=[]
	for i in range(len(f)):
		l.append(f[i].user)
	item_list=ItemModel.objects.filter(user__in=l)
	return item_list