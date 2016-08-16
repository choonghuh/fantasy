from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.conf import settings
playerdb = settings.JS_DATABASE['players']

from django.template import loader

import json

def home(request):
	template = loader.get_template('lobby.html')
	context = {'player_list':playerdb}
	return HttpResponse(template.render(context, request))
