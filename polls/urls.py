from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('profile/', views.profile, name='profile'),
    path('near_by_searches/', views.near_by_searches, name='near_by_searches'),
    # searches/は任意でカンマ区切りの座標を受け取る
    path('popular_searches/<str:query_geolocation>/<str:cuisine>/', views.popular_searches, name='popular_searches'),
    path('searches/', views.searches, name='searches'),
    path('user_rating_count_searches/<str:query_geolocation>/<str:cuisine>/', views.user_rating_count_searches, name='user_rating_count_searches'),
    path('niche_searches/<str:query_geolocation>/<str:cuisine>/', views.niche_searches, name='niche_searches'),
]
