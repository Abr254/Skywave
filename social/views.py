from django.shortcuts import render
# views.py

from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Message, Reply
from .forms import MessageForm, MediaForm

@login_required
def home(request):
    messages = Message.objects.all().order_by('-created_at')
    message_form = MessageForm()
    media_form = MediaForm()
    context = {
        'messages': messages,
        'message_form': message_form,
        'media_form': media_form,
    }
    return render(request, 'social_page.html', context)

@login_required
def reply_to_message(request, message_id):
    if request.method == 'POST':
        message = Message.objects.get(pk=message_id)
        content = request.POST.get('content')
        Reply.objects.create(user=request.user, message=message, content=content)
        return redirect('home')
    else:
        return redirect('home')

@login_required
def like_message(request):
    if request.method == 'POST':
        message_id = request.POST.get('message_id')
        message = Message.objects.get(pk=message_id)
        message.likes += 1
        message.save()
        return redirect('home')
    else:
        return redirect('home')

@login_required
def create_message(request):
    if request.method == 'POST':
        message_form = MessageForm(request.POST, request.FILES)
        if message_form.is_valid():
            new_message = message_form.save(commit=False)
            new_message.user = request.user
            new_message.save()
            return redirect('home')
    else:
        message_form = MessageForm()
    context = {
        'message_form': message_form,
    }
    return render(request, 'social_page.html', context)

# Create your views here.
