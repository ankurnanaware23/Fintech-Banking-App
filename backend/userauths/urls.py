# users/urls.py

from django.urls import path
from userauths import views

urlpatterns = [
    path('auth/register/', views.RegisterView.as_view(), name='register'),
    path('auth/login/', views.LoginView.as_view(), name='login'),
    path('auth/logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', views.UserView.as_view(), name='user'), # Endpoint to get user details
    
    # Use our custom refresh view that handles cookies
    path('auth/token/refresh/', views.CookieTokenRefreshView.as_view(), name='token_refresh'),
]