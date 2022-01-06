from django.urls import path 
from .views import HomePage, AboutPage, ContactUs     #pull HomePage function from views

urlpatterns = [
    path('', HomePage,name='home-page'), 
    path('about/', AboutPage,name='about-page'),
    path('contact/', ContactUs,name='contact-page')
]