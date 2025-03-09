
from django.contrib import admin
from django.urls import path,include
#for showing templates
from django.conf import settings
from django.contrib.staticfiles.urls import  staticfiles_urlpatterns,static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Shop_App.urls')),
    path('account/',include('Login_App.urls')),
    
    
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
