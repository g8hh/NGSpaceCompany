# -*- coding: utf-8 -*-

from django.urls import path

from rest_framework.authtoken import views as drf_views 

from .views import register
from .views import post
from .views import data



################################################################################
urlpatterns = [
	#---------------------------------------------------------------------------
    path('login/', drf_views.obtain_auth_token),
    path('register/', register.RegisterView.as_view()),
	#---------------------------------------------------------------------------
    path('post/', post.PostView.as_view()),
	#---------------------------------------------------------------------------
    path('ranks/', data.RanksView.as_view()),
    path('stats/', data.StatsView.as_view()),
	#---------------------------------------------------------------------------
]
################################################################################