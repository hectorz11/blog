# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Categoria(models.Model):
	categoria 	= models.CharField(max_length=75, verbose_name='Categoria')
	slug		= models.SlugField(max_length=200)

	def __unicode__(self):
		return self.categoria

	def get_absolute_url(self): # Link permanente para nuestra categoria
		return '/%s' % self.slug