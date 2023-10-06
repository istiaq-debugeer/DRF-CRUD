from django.contrib import admin
from . import models
from blog_Api.models import Student
# Register your models here.

@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title','id','status','slug','content')
    prepopulated_fields = {'slug':('title',),}


    admin.site.register(models.Category)



admin.site.register(Student)