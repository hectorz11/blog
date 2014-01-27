from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'posts.views.blogHomePage', name='home'),
    url(r'^categoria/(?P<slug>[-\w]+)/$', 'categorias.views.getCategoria', name='categoria'),
    url(r'^categorias/$', 'categorias.views.categoriasIndex', name='categorias'),
    url(r'^blog$', 'posts.views.blog', name='blog'),
    url(r'^(?P<anio>\d{4})/(?P<mes>\w{3})/(?P<dia>\d{2})/(?P<slug>[-\w]+)/(?P<id>\d+)/$', 'posts.views.getPost', name='post'),
    (r'^public/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'/home/hector/ProjectDjango/blog/public'}),
    url(r'^admin/', include(admin.site.urls)),
)
