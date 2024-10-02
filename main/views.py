from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.views import View
from django.db.models import Q
from .forms import CustomUserCreationForm, PostForm, MediaUploadForm
from .models import MediaItem, Post, Message
from django.contrib.auth.models import User
from main.models import Profile  # Make sure to replace 'your_app' with your actual app name
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from .forms import MediaUploadForm  # Ensure this form is defined
@login_required
def upload_media(request):
    if request.method == 'POST':
        form = MediaUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('some_view')  # Adjust this to your needs
    else:
        form = MediaUploadForm()
    return render(request, 'upload_media.html', {'form': form})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Adjust this as needed
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        messages.success(request, "Your account has been deleted successfully.")
        return redirect('home')  # Redirect to a homepage or login page
    return render(request, 'delete_account.html')
def social_page(request, user_id):
    users = User.objects.exclude(id=request.user.id)  # Exclude current user
    online_friends = []

    # Access profile safely
    if hasattr(request.user, 'profile'):
        online_friends = request.user.profile.friends.all()

    return render(request, 'social/social_page.html', {
        'users': users,
        'online_friends': online_friends,
        'user_id': user_id,
    })
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def registerUser(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully. You can now log in.')
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def loginUser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email and password:
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Email or Password is Incorrect')
        else:
            messages.error(request, 'Fill out all the fields')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')
def media_gallery(request):
    if request.method == 'POST':
        form = MediaUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MediaUploadForm()

    media_items = MediaItem.objects.all()
    return render(request, 'media.html', {'form': form, 'media_items': media_items})
class UserListView(ListView):
    model = User
    template_name = 'users.html'
    context_object_name = 'users'

class UserDetailView(DetailView):
    model = User
    template_name = 'users.html'
    context_object_name = 'user'

class MessageUserView(View):
    def get(self, request, recipient_id):
        recipient = get_object_or_404(User, id=recipient_id)
        messages = Message.objects.filter(
            Q(user=request.user, recipient=recipient) | 
            Q(user=recipient, recipient=request.user)
        ).order_by('created_at')

        return render(request, 'social_page.html', {'recipient': recipient, 'messages': messages})

    def post(self, request, recipient_id):
        content = request.POST.get('content')
        recipient = get_object_or_404(User, id=recipient_id)

        message = Message(user=request.user, recipient=recipient, content=content)
        message.save()

        return redirect('social_page', recipient_id=recipient.id)

def send_message(request, pk):
    recipient = get_object_or_404(User, pk=pk)
    
    if request.method == 'POST':
        message = request.POST.get('message', '')
        # Code to send the message goes here
        messages.success(request, f'Message sent to {recipient.username}')
        return redirect('user_detail', pk=pk)
    
    return render(request, 'send_message.html', {'recipient': recipient})

def social_page(request, user_id):
    users = User.objects.exclude(id=request.user.id)  # Exclude current user
    online_friends = request.user.profile.friends.all()  # Adjust based on your model structure

    return render(request, 'social/social_page.html', {
        'users': users,
        'online_friends': online_friends,
        'user_id': user_id,
    })

# Create your views here.
