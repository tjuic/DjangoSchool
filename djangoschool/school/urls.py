from django.urls import path 
from .views import HomePage, AboutPage     #pull HomePage function from views

urlpatterns = [
    path('', HomePage,name='home-page'), 
    path('about/', AboutPage,name='about-page')
]