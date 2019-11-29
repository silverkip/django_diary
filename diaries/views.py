from django.shortcuts import render, redirect
from .models import Diary
from django.http import Http404
from datetime import datetime

def top(request): #Top page
    return render(request, 'diaries/top.html')

def index(request):
    entries = Diary.objects.all()
    context = {
        'entries': entries, 
    }
    return render(request, 'diaries/index.html', context)

def write(request):
    if request.method == "POST":
        entry = Diary.objects.create(
            title=request.POST['title'],
            date=request.POST['time'],
            created=datetime.now(),
            content=request.POST['content'],
            )
        return redirect('detail', entry.id)
    return render(request, 'diaries/write.html')

def update(request, diary_id):
    try:
        entry = Diary.objects.get(pk=diary_id)
    except Diary.DoesNotExist:
        raise Http404("Entry does not exist.")
    if request.method == "POST":
        entry.content = request.POST['content']
        entry.title = request.POST['title']
        entry.edited = datetime.now()
        entry.save()
        return redirect('detail', diary_id)
    context = {
        'entry': entry,
    }
    return render(request, 'diaries/update.html', context)

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
    return redirect('entries')