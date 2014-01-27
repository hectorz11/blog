from django.shortcuts import render_to_response, Http404
from django.template import RequestContext
from categorias.models import Categoria 
from posts.models import Post

"""
Primer Vsita: listar categorias
"""

def categoriasIndex(request):
	try:
		categorias = Categoria.objects.all()
	except Categoria.DoesNotExist:
		categorias = None
	ctx = {'categorias':categorias}
	return render_to_response('categorias.html',ctx, context_instance = RequestContext(request))

"""
Segunda Vista: listar los posts de categoria x
"""

def getCategoria(request,slug):
	try:
		categoria 	= Categoria.objects.get(slug=slug)
		posts		= Post.objects.filter(categoria=categoria)
	except Categoria.DoesNotExist:
		return Http404
	ctx = {'categoria':categoria,'posts':posts}
	return render_to_response('posts_categoria.html',ctx, context_instance = RequestContext(request))