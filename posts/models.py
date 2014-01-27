from django.db import models
from django.contrib.auth.models import User
from categorias.models import Categoria

# Create your models here.

"""
Esta es la clase que se encarga de crear nuestra tabla y la cual invocaremos usando el ORM, para tener acceso
a las estradas de posts
"""

class Post(models.Model):
	titulo		= models.CharField(max_length=100, verbose_name='Titulo de entrada')
	slug		= models.SlugField(max_length=200, help_text='Este campo se autocompleta con el titulo')
	categoria 	= models.ForeignKey(Categoria)
	autor		= models.ForeignKey(User)
	contenido	= models.TextField(verbose_name='Contenido de la entrada')
	fecha		= models.DateTimeField(auto_now=False, auto_now_add=True, editable=False)
	publicar	= models.BooleanField(default=False)

	def __unicode__(self):
		return self.titulo

	class Meta:
		ordering			= ['-fecha'] # Ordenamos los post en el admin
		verbose_name_plural = 'Post'	# El plural es importante, muchas veces, no se le puede dejar a Django que lo asigne (amistad -> amistads)

"""
Esta funcion se encarga de crear un url absoluto para nuestra entrada
"""		

def get_absolute_url(self):
	return '/%s/%s/' % (self.fecha.strftime("%Y/%b/%d").lower(),self.slug) # Existe muchas formas para hacer esto