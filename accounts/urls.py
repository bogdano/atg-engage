from django.contrib import admin
from django.urls import path
from . import views #new 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send-login-link/', views.send_login_link, name='send_login_link'), # new
    path('login/<str:uidb64>/<str:token>/', views.login_with_link, name='login_with_link'), #New
    path('user-email/', views.user_email, name='user_email'), #new
]