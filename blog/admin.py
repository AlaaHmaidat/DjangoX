from django.contrib import admin
from .models import Blog

# Register your models here.


class CustomBlogAdmin(admin.ModelAdmin):
    model= Blog
    list_display = ['title', 'author',]
    fieldsets= (
        ('Auth Info',{
            'fields':('author',
            )}
        ),
        ('post Info',{
            'fields':('post',
            )}
        ),
    )
    
admin.site.register(Blog, CustomBlogAdmin)
