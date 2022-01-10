from django.urls import path 
from .views import *     #pull HomePage function from views, * all

urlpatterns = [
    path('', HomePage,name='home-page'), 
    path('about/', AboutPage,name='about-page'),
    path('contact/', ContactUs,name='contact-page'),
    path('score/', ShowScore,name='score-page')
]