from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.conf import settings
playerdb = settings.JS_DATABASE['players']

from django.template import loader

from fantasy.models import Player

import json

from django.views.decorators.csrf import csrf_exempt

def home(request):
	print "print works"
	template = loader.get_template('lobby.html')
	context = {'player_list':playerdb, 'player_list_raw':json.dumps(playerdb)}
	return HttpResponse(template.render(context, request))

@csrf_exempt
def add_player(request):
	print "[add_player]"
	print request
	print request.body
	print request.POST
	newPlayerData = json.loads(request.body)
	player = Player.objects.create(first_name=newPlayerData['first_name'],\
									last_name=newPlayerData['last_name'],\
									position=newPlayerData['position'])
	print player.id
	return HttpResponse(status=200)
