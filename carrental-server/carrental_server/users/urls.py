from django.urls import path
from . import views

# Defines the end points for user creation and blacklisting JWT tokens
urlpatterns = [
    path('register/', views.CustomUserCreate.as_view(), name='register'),
    path('blacklist/', views.BlacklistTokenUpdateView.as_view(), name='blacklist'),
]