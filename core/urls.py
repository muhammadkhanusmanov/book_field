
from django.contrib import admin
from django.urls import path,include
from apis.views import CustomAPIView,RegisterUser,LoginUser
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/user/',RegisterUser.as_view()),
    path('login/user/',LoginUser.as_view()),
    path('accounts/', include('allauth.urls')),
    path('accounts/google/login/callback/home/', CustomAPIView.as_view()),
    path('page/',CustomAPIView.as_view())
]
