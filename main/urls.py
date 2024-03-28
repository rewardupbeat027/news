from . import views
from django.urls import path

urlpatterns = [path('addnews/', views.addnews, name='addnews'),
               path('main/', views.index, name="main"),
               path('accounts/profile/', views.news, name="news"),
               path('<int:pk>', views.MyDetailView.as_view(), name='mydetail'),
               path('img/', views.my_view, name='img'),
               path('cookie/', views.set_cookie, name='cookie'),
               path('delcookie/', views.deletecookie, name='delcookie'),
               path('registr/', views.UserRegister.as_view(), name='registr'),
               path('<slug:slug>/', views.addnews, name='slug'),
               path('logout/', views.logout, name='logout')
               ]