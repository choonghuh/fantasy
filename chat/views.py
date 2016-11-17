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
	playerlist = build_playerlist()
	context = {'player_list':playerlist, 'player_list_raw':json.dumps(playerdb)}
	return HttpResponse(template.render(context, request))

def build_playerlist():
	returnlist = []
	plist = Player.objects.all()
	for player in plist:
		aa={}
		aa['first_name'] = player.first_name
		aa['last_name'] = player.last_name
		aa['position'] = player.position
		returnlist.append(aa)
	return returnlist

@csrf_exempt
def add_player(request):
	print "[-------------------------------- add_player -----------------------------------]"
	print request
	# print request.body
	print request.message.content
	newPlayerData = json.loads(request.message.content['body'])
	player = Player.objects.create(first_name=newPlayerData['first_name'],\
									last_name=newPlayerData['last_name'],\
									position=newPlayerData['position'])
	print player.id
	return HttpResponse("OK",status=200)

def testview(request):
	print "[testview]"
	return HttpResponse("its all good")