from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"


def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})
