from django.contrib import admin
from .models import Post

#Getting the Post model on the admin site
admin.site.register(Post)
