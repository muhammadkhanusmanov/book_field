
from django.contrib import admin
from django.urls import path,include
from apis.views import CustomAPIView,RegisterUser
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/user/',RegisterUser.as_view()),
    path('accounts/', include('allauth.urls')),
    path('accounts/google/login/callback/home/', CustomAPIView.as_view()),
    path('page/',CustomAPIView.as_view()),
]
