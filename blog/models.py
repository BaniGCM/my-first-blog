from django.db import models
from django.utils import timezone

class Post (models.Model):
	author = models.ForeignKey('auth.user')
	title = models.CharField(max_length=150)
	text = models.TextField()
	created_date = models.DateField(default=timezone.now)
	publish_date = models.DateTimeField(blank=False, null=False)
	def publish(self):
		self.published_date = timezone.now ()
		self.save
	def __str__(self):
		return self.title
