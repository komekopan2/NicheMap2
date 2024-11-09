from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('map/', views.map, name='map'),
    path('near_by_searches/', views.near_by_searches, name='near_by_searches'),
    # searches/は任意でカンマ区切りの座標を受け取る
    path('searches/<str:query_geolocation>/', views.searches_with_geolocation, name='searches_with_geolocation'),
    path('searches/', views.searches, name='searches'),
    path('user_rating_count_searches/<str:query_geolocation>/', views.user_rating_count_searches_with_geolocation, name='user_rating_count_searches_with_geolocation'),
]
