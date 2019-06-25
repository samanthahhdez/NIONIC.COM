from django.urls import path
from nionic_app import views

app_name = 'nionic_app'
urlpatterns = [
    path ('nionic_app',views.index,name='index'),
]
