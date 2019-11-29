from django.shortcuts import render, redirect
from .models import Diary, User
from django.http import Http404
from datetime import datetime
from django.contrib import messages

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
        user_id = request.POST['editing_user']
        user = User.objects.get(pk=user_id)
        entry = Diary.objects.create(
            title=request.POST['title'],
            date=request.POST['time'],
            created=datetime.now(),
            content=request.POST['content'],
            user=user,
            )
        messages.success(request, "Entry Posted!")
        return redirect('detail', entry.id)
    context = {
        'users' : User.objects.order_by('id'),
    }
    return render(request, 'diaries/write.html', context)

def update(request, diary_id):
    try:
        entry = Diary.objects.get(pk=diary_id)
        user = entry.user
    except Diary.DoesNotExist:
        raise Http404("Entry does not exist.")
    if request.method == "POST":
        if request.POST['editing_user'] != str(user.id):
            messages.error(request, "You're not the owner of this diary entry!")
        else:
            entry.content = request.POST['content']
            entry.title = request.POST['title']
            entry.edited = datetime.now()
            entry.save()
            messages.success(request, "Successfully edited your entry.")
            return redirect('detail', diary_id)
    context = {
        'entry': entry,
        'users': User.objects.order_by('id'),
    }
    return render(request, 'diaries/update.html', context)

def details(request, diary_id):
    try:
        entry = Diary.objects.get(pk=diary_id)
        user = entry.user
    except Diary.DoesNotExist:
        raise Http404("Entry does not exist.")
    context = {
        'entry': entry,
        'user' : user,
    }
    return render(request, 'diaries/detail.html', context)

def delete(request, diary_id):
    try:
        entry = Diary.objects.get(pk=diary_id)
    except Diary.DoesNotExist:
        raise Http404("Entry does not exist.")
    entry.delete()
    messages.success(request, "Entry Deleted Successfully")
    return redirect('entries')