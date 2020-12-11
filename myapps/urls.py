from django.urls import path

from . import views # mysite/myapp/views.pyをインポート

from django.contrib.auth import views as auth_views

#app_name = 'myapp'
urlpatterns = [
    path('home/', views.IndexView.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='myapps/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('test/',views.TestView.as_view(),name='test'),
]