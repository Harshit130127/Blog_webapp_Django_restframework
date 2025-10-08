from django.contrib import admin
from .models import Post
# Register your models here.


# to customize the admin interface( post model customization)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=["title","created"]
    
    list_filter=["created"]