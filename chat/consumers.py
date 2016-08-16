from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group

def ws_connect(message):
	print "someone connected"
	Group('chatroom1').add(message.reply_channel)

def ws_message(message):
	print "someone said " + message['text']
	chatdict = {'text': message['text']}
	Group('chatroom1').send(chatdict)

def ws_disconnect(message):
	Group('chatroom1').discard(message.reply_channel)