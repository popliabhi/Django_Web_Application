# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import redirect, render_to_response
from .forms import HomeForm
from .models import my_blog
from django.views.decorators.csrf import csrf_protect, csrf_exempt


@csrf_exempt
def form_view(request):
	c={}
	form=HomeForm(request.POST)
	 		
	if request.method =="POST":
		form=HomeForm(request.POST)
		if form.is_valid():
			form.save()
			if not request.is_ajax():
				form = HomeForm()
				return render_to_response('home.html',{'form':form, 'data':my_blog.objects.all()})
	else:
		form = HomeForm()
	
	return render_to_response('home.html',{'form':form,'data':my_blog.objects.all()},c)


