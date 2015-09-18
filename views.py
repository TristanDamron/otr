from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from .models import *
import os
from datetime import datetime

def getcurrent(show):
    date = datetime.now()
    tmp = None

    print date.hour
    
    for i in range(0, len(show)):
        if show[i].time_slot_from == date.hour:
            tmp = show[i]
            print show[i].show_name
            return tmp
            

def otr(request):
    try:
        show = Show.objects.order_by('time_slot_from')[:24]    
        current_show = getcurrent(Show.objects.all())
        current_audio = current_show.audio_files.audio_file.url
        header = Header.objects.all()
        news = News.objects.order_by('number')[:2]
        template = loader.get_template('otr.html')
        context = RequestContext(request, {
            'current_show': current_show,
            'current_audio': current_audio,
            'show': show,
            'header': header[0],
            'news': news,
        })
        return HttpResponse(template.render(context))
    except:
        show = Show.objects.order_by('time_slot_from')[:24]
        header = Header.objects.all()
        news = News.objects.order_by('number')[:2]
        template = loader.get_template('offline.html')
        context = RequestContext(request, {
            'show': show,
            'header': header,
            'news': news,
        })
        return HttpResponse(template.render(context))

def broadcast(request):
    template = loader.get_template('broadcast.html')
    return HttpResponse(template.render())
