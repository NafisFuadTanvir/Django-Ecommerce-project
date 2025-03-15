from django.urls import path
from Login_App import views
app_name='Login_App'

urlpatterns = [
    
    path('signup/',views.sign_up,name='signup'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.login_user,name='logout'),
    path('profile/',views.user_profile,name='profile')
    
]