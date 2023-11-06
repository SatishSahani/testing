from django.contrib import admin
from django.urls import path, include
from home import views

from django.contrib import admin
from django.urls import path,include
# from ganalytics.views import Analytics_Dashboard, Analytic_Dasboard
# from gadwords.views import ad_page,Adwords_Dashboard
# from Meta.views import meta_data
# from ganalytics.views import analytics_data


urlpatterns = [ 
    path('',views.index, name="home"),
    path('login',views.loginUser, name="login"),
    path('logout',views.logoutUser, name="logout"),
    path('signup/', views.signup, name='signup'),
    
   

]
    
