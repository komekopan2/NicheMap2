from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('map/', views.map, name='map'),
    path('near_by_searches/', views.near_by_searches, name='near_by_searches'),
    path('searches/', views.searches, name='searches'),
]
