from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.roomView),#set a pattern for urls within the classApp App.
    path('test/',views.get_stories),
    path('login/',auth_views.LoginView.as_view()),
    path('register/',views.registerView),
    path('logout/',views.logoutView),
    path('Data_Visualization/',views.get_data, name="data-view"),
    path('charts/',views.chartView),
]