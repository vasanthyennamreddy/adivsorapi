from django.urls import path,include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('',views.apibase,name='apibase'),
    path('advisor',views.create_advisor,name='create_advisor'),
    path('user/register',views.register,name='register'),
    path('user/login',obtain_auth_token,name='login'),
    path('user/<int:userid>/advisor',views.getlist,name='advisorlist'),
    path('user/<int:userid>/advisor/<int:advid>',views.bookcall,name='bookcall'),
    path('user/<int:userid>/advisor/booking',views.booking,name="booking"),
    
    
]
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
