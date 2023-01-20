from django.urls import path
from . import views
app_name='digitalClock_app'


urlpatterns=[
    path('',views.digitalClock_app_index,name='index'),
]