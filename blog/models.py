from django.db import models
from django.utils import timezone

class Post (models.Model):
	author = models.ForeignKey('auth.user')
	title = models.CharField(max_length=150)
	text = models.TextField()
	created_date = models.DateField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	def published(self):
		self.published_date = timezone.now ()
		self.save
	def __str__(self):
		return self.title
