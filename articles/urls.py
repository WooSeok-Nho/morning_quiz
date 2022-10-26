from django.urls import path
from articles import views

urlpatterns = [
    path('index/',views.index.as_view(),name='index' ),
]
