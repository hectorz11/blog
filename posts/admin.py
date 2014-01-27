from posts.models import Post
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("titulo",)}

admin.site.register(Post,PostAdmin)