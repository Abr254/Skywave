from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import UserListView, MessageUserView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import media_gallery

urlpatterns = [
    path('media/', media_gallery, name='media'),
    path('', views.home, name='home'),  
    path('index/', views.index, name='index'),# User Registration and Authentication
    path('signup/', views.registerUser, name='signup'),  
    path('login/', views.loginUser, name='login'),  
    path('logout/', views.logout_view, name='logout'),  

    # Social and User related views
    path('social/', views.social_page, name='social_page'),  
    path('social/<int:user_id>/', views.social_page, name='social_page_user'),  # Update for clarity
    path('users/', UserListView.as_view(), name='users'),
    path('user/<int:pk>/', views.UserDetailView.as_view(), name='users'),
    path('user/<int:pk>/message/', views.send_message, name='social_page'),

    # Messaging
    path('message/<int:recipient_id>/', MessageUserView.as_view(), name='social_page'),

    # Media Upload and Display
   #path('upload/', views.upload_media, name='upload_media'),  
    path('media/', views.media_gallery, name='media'),  
    # other paths...
    path('delete-account/', views.delete_account, name='delete_account'),  # Ensure delete_account is correctly referenced
    path('upload-media/', views.upload_media, name='upload_media'),  # URL for media upload
    path('create-post/', views.create_post, name='media_gellery'),      
  
    # Password Reset views
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)