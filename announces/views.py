from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView

from .models import Announce, Reply
# Create your views here.
class AnnounceList(ListView):
    model = Announce
    template_name = 'announces/announces.html'
    context_object_name = 'announces'

class AnnounceDetail(DetailView):
    model = Announce
    template_name = 'announces/announcedetail.html'
    context_object_name = 'announce'

def reply_to_announce(request, pk):
    if request.method == "POST":
        user = request.user
        announce = Announce.objects.get(id=pk)
        content = request.POST['content']
        reply = Reply.objects.create(announce=announce, content=content, replier=user)
        reply.save()
        return HttpResponseRedirect('/announces/')
    else:
        print('error')
    return render(request, 'announces.html')




