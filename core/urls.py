
from django.contrib import admin
from django.urls import path,include
from apis.views import HomePage,CustomAPIView
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('home/', TemplateView.as_view(template_name='login.html'), name='home'),
    path('accounts/google/login/callback/home/', HomePage.as_view()),
    path('page/',CustomAPIView.as_view()),
]
