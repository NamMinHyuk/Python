from django.urls import path
from . import views
from django.urls.conf import include


urlpatterns = [
    path('', views.hello),
    path('var01', views.var01),
    path('var02', views.var02),
]