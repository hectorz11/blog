# -*- coding: utf-8 -*-
import datetime
import time
from posts.models import Post
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

"""
Primera Vista: index / home de nuestro blog, aqui haremos uso del ORM de Django para accesar a los ultimos posts 
"""

def blogHomePage(request):
	try:
		posts = Post.objects.filter(publicar=True).order_by("-id")[0:3]
	except Post.DoesNotExist:
		posts = None
	ctx = {'posts':posts}
	return render_to_response('index.html',ctx,context_instance = RequestContext(request))

"""
Segunda Vista: accesamos un post x, notar los argumentos pasados a la vista, podriamos solo usar request, slug, pero
como no hemos hecho un slug unico, tendriamos problemas con dos post que posean el mismo slug, luego veremos
como hacer un slug unico, por ahora, accesaremos el post usando el slug y el id a la vez
"""

def getPost(request,anio,mes,dia,slug,id):
	date_stamp	= time.strptime(anio + mes + dia, "%Y%b%d")
	fecha		= datetime.date(*date_stamp[:3])
	entrada		= get_object_or_404(Post,
					fecha_year=fecha.year,
					fecha_mosth=fecha.month,
					fecha_day=fecha.day,
					pk=id,
					slug=slug,
					publicar=True)
	ctx = {'post':entrada}
	return render_to_response('post.html',ctx,context_instance = RequestContext(request))

"""
Tercera Vista: desplegando todos los post del blog
"""

def blog(request):
	try:
		posts = Post.objects.filter(publicar=True).order_by("-id")
	except Post.DoesNotExist:
		posts = None
	ctx = {'posts':posts}
	return render_to_response('blog.html',ctx,context_instance = RequestContext(request))