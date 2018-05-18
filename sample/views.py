# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from sample.models import Message

# Create your views here.
class MessageList(ListView):
	"""
	This view is responsible to display messages
	"""
	model = Message

# I tried to use the @csrf_protect for secure purpose. But got errors in that.
# So I used @csrf_exempt, but it is not secure.
@csrf_exempt 
def add_message(request):
	post_data = request.POST
	create_message = Message.objects.create(name=post_data["name"], message=post_data["message"])
	return HttpResponseRedirect(reverse('message_list'))
 

@csrf_exempt
def delete_message(request, id):
	message = Message.objects.get(id=id)
	message.delete()
	return HttpResponseRedirect(reverse('message_list'))


@csrf_exempt
def edit_message(request):
	post_data = request.POST
	edit_message = Message.objects.get(id=post_data["update_id"])
	edit_message.name = post_data["name"]
	edit_message.message = post_data["message"]
	edit_message.save()
	return HttpResponseRedirect(reverse('message_list'))
