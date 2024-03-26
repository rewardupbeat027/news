from . import views
from django.urls import path

urlpatterns = [path('addnews/', views.addnews, name='addnews'),
               path('main/', views.index, name="main"),
               path('accounts/profile/', views.news, name="news"),
               path('<int:pk>', views.MyDetailView.as_view(), name='mydetail'),
               path('img/', views.my_view),
               path('cookie/', views.set_cookie),
               path('delcookie/', views.deletecookie),
               path('registr/', views.UserRegister.as_view()),
               path('<slug:slug>/', views.addnews),
               path('logout/', views.logout)
               ]