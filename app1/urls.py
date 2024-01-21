from django.urls import path,include
from app1.views import *

urlpatterns = [
    path('',index_home,name='home'),
    path('abilities/',index_abilities,name='abilities'),
    path('contact/',index_contact,name='contact'),
    path('education/',index_education,name='education'),
    path('languages/',index_languages,name='languages')
]
