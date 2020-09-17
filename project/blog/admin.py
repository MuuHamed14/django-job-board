from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_filter = ['active', 'created_by', 'created_at']
    list_display = ['title', 'active', 'created_by', 'created_at']
    search_fields = ['title', 'content']


admin.site.register(Post,PostAdmin)
