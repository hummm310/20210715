from django.db import models
from django.utils import timezone

class Post(models.Model):
	title = models.CharField(max_length=200) #field=資料欄
	content = models.TextField() #TextField=大量文字沒限制
	pub_date = models.DateTimeField(default=timezone.now) #預設現在的時間
	class Meta:
		ordering = ('-pub_date',) 
	def __str__(self):
		return self.title

#ctrl+x刪掉整列
class Country(models.Model):
	country_id = models.IntegerField()
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name

class City(models.Model):
	name = models.CharField(max_length=50)
	population = models.IntegerField()
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	def __str__(self):
		return self.name

class Note(models.Model):
	title = models.CharField(max_length=200)
	pub_date = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.title