from django.urls import path

from chat.views import chat_view, room_view

urlpatterns = [
    path("", chat_view),
    path("<str:room_name>/", room_view, name="room")
]
