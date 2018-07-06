from django.db import models
from datetime import datetime
from django.contrib.postgres.fields import JSONField

class ChatModel(models.Model):
	'''
		To save the chat logs for a particular chat room
	'''
	chat_group_name = models.CharField(
		max_length=100,
	)

	chat_log = models.TextField()

	def __str__(self):
		return self.chat_group_name


class ComponentJson(models.Model):

	date = models.DateTimeField(
		default=datetime.now(),
		blank=True,
		null=True
	)

	name = models.CharField(
		max_length=100,
		blank=True,
		null=True,
	)

	json_data = JSONField()

	site_thumb = models.TextField(
		blank=True,
		null=True
	)

	def __str__(self):
		return self.name

class ThumbnailData(models.Model):
	thumbnail_name = models.CharField(
		max_length=200,
		blank=True,
		null=True
	)

	thumbnail_title = models.CharField(
		max_length=200,
		blank=True,
		null=True
	)

	thumbnail_content = models.TextField(
		blank=True,
		null=True
	)

	def __str__(self):
		return self.thumbnail_name