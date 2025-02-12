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
    path('popular_searches/', views.popular_searches, name='popular_searches'),
    path('searches/', views.searches, name='searches'),
    path('user_rating_count_searches/', views.user_rating_count_searches, name='user_rating_count_searches'),
    path('searches3/', views.searches3, name='searches3'),
    path('niche_searches/', views.niche_searches, name='niche_searches'),
    path('niche_post/', views.niche_post, name='niche_post'),
]
