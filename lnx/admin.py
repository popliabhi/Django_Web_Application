# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import my_blog
from django.contrib import admin

# Register your models here.


class MyBlogAdmin(admin.ModelAdmin):
	list_display = ['author','title','description','pub_date']

admin.site.register(my_blog,MyBlogAdmin)