from django.shortcuts import render, redirect
from .models import Diary
from django.http import Http404

def top(request): #Top page
    return render(request, 'diaries/top.html')

def index(request):
    entries = Diary.objects.all()
    context = {
        'entries': entries, 
    }
    return render(request, 'diaries/index.html', context)

def details(request, diary_id):
    try:
        entry = Diary.objects.get(pk=diary_id)
    except Diary.DoesNotExist:
        raise Http404("Entry does not exist.")
    context = {
        'entry': entry,
    }
    return render(request, 'diaries/detail.html', context)

def delete(request, diary_id):
    try:
        entry = Diary.objects.get(pk=diary_id)
    except Diary.DoesNotExist:
        raise Http404("Entry does not exist.")
    entry.delete()
    return redirect(entries)