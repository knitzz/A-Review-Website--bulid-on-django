from django.db import models

# Create your models here.
from django.conf import settings




User= settings.AUTH_USER_MODEL

class ItemModel(models.Model):
	user=models.ForeignKey(User)
	title=models.CharField(max_length=100,blank=False,null=False)
	review=models.TextField(blank=False)
	image=models.ImageField(upload_to='item_image',blank=True)
	tags=models.TextField(blank=True)
	rating=models.IntegerField(blank=False)

	def __str__(self):
		return self.title

	def get_tags(self):
		return self.tags.split(',')

	def return_rating(self):
		return range(self.rating)

	def return_notrating(self):
		return range(5-self.rating)

	
