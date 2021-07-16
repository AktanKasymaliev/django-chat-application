from chat.models import Message
from django.shortcuts import render

def chat_view(request):
    return render(request, "chat/chat.html")

def room_view(request, room_name):
    username = request.GET.get("username", "Anonymous")
    messages = Message.objects.filter(room=room_name)[0:25]
    context = {
        "username": username,
        "room_name": room_name,
        "messages": messages
    }
    return render(request, "chat/room.html", context)