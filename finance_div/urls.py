from django.urls import path
from . import views

urlpatterns = [
   # path('Student/', views.Student, name = 'Student' ),
    path('tests/', views.tests, name = 'tests' ),
    ]