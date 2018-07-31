from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
print(dir(auth_views))


urlpatterns = [
   path('accounts/login/', views.login,name='login'),
   path('accounts/register/', views.register , name='register'),
   path('dashboard/',views.dashboard,name='dashboard'),
   # path('accounts/register/', auth_views.RegisterView.as_view()),
   
   path('graph',views.graph,name='graph'),

   path('',views.index,name='index'),
   # path('',views.index,name='index'),
   # path('',views.index,name='index'),
]
