from posts.models import Categoria
from django.contrib import admin

class CategoriaAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("categoria",)}

admin.site.register(Categoria,CategoriaAdmin)