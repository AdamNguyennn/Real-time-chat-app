from os import name
from django.core.checks import messages
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from appChat.models import Room, Message

# Create your views here.
def index(request):
	return render(request, 'index.html')



def checkview(request):
	room = request.POST['room_name']
	username = request.POST['username']

	if Room.objects.filter(name=room).exists():
		return redirect('/'+room+'/?username='+username)
	else:
		new_room = Room.objects.create(name=room)
		new_room.save()
		return redirect('/'+room+'/?username='+username)


def room(request, room):
	username = request.GET.get('username')
	room_details = Room.objects.get(name=room)
	return render(request, 'room.html', {
		'username':username,
		'room':room,
		'room_details':room_details
	})


def send(request):
	username = request.POST['username']
	message = request.POST['message']
	room_id = request.POST['room_id']

	NewMessage = Message.objects.create(value=message, user=username, room=room_id)
	NewMessage.save()
	return HttpResponse('Oke roi do')


def getMessages(request, room):
	room_details = Room.objects.get(name=room)

	messages = Message.objects.filter(room=room_details.id)
	return JsonResponse({'messages': list(messages.values())})

