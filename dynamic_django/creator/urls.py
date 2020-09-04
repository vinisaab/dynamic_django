from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='hello'),
    path('page/<str:target>/', views.page, name='page')
]
