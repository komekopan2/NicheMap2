# Create your views here.
from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .method.nearby_search_api import nearby_search_api
from .method.nearby_search_db import nearby_search_db
from .method.saving_restaurants import saving_restaurants
from .method.select_icon import select_path_icon, select_cuisine_icon
from allauth.socialaccount.models import SocialAccount


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    template = loader.get_template('polls/detail.html')
    context = {
        'question': question
    }
    return HttpResponse(template.render(context, request))


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


@login_required
def profile(request):
    # 現在のログインユーザーのGoogleアカウント情報を取得
    template = loader.get_template('polls/profile.html')
    try:
        google_account = SocialAccount.objects.get(user=request.user, provider='google')
        profile_data = google_account.extra_data
        # 例: name、email、pictureなどのプロファイル情報
        context = {
            'name': profile_data.get('name'),
            'email': profile_data.get('email'),
            'picture': profile_data.get('picture'),
            'profile_data': profile_data,
        }
    except SocialAccount.DoesNotExist:
        # Googleアカウントがない場合
        context = {
            'error': 'Googleアカウント情報が見つかりません。',
        }

    return HttpResponse(template.render(context, request))


@login_required
def near_by_searches(request):
    template = loader.get_template('polls/near_by_searches.html')
    context = {
        'front_maps_api_key': settings.FRONT_MAPS_API_KEY,
    }
    return HttpResponse(template.render(context, request))


@login_required
def searches(request):
    template = loader.get_template('polls/searches.html')
    context = {
        'front_maps_api_key': settings.FRONT_MAPS_API_KEY,
    }
    return HttpResponse(template.render(context, request))


@login_required
def popular_searches(request, query_geolocation, cuisine):
    # 文字列をカンマで分割してfloatに変換
    geolocation = {'lat': float(query_geolocation.split(',')[0]), 'lng': float(query_geolocation.split(',')[1]),
                   'zoom': float(query_geolocation.split(',')[2])}
    try:
        restaurants = nearby_search_api(geolocation, cuisine)['places']
    except KeyError:
        saved_restaurants = []
    else:
        top_searches_restaurants = restaurants[:3]
        saved_restaurants = saving_restaurants(top_searches_restaurants)
    print(saved_restaurants)
    path = 'popular_searches'
    path_icon = select_path_icon(path)
    cuisine_icon = select_cuisine_icon(cuisine)
    template = loader.get_template('polls/popular_searches.html')
    context = {
        'front_maps_api_key': settings.FRONT_MAPS_API_KEY,
        'geolocation': geolocation,
        'cuisine': cuisine,
        'saved_restaurants': saved_restaurants,
        'path': path,
        'color': 'primary',
        'path_icon': path_icon,
        'cuisine_icon': cuisine_icon,
    }
    return HttpResponse(template.render(context, request))


@login_required
def user_rating_count_searches(request, query_geolocation, cuisine):
    # 文字列をカンマで分割してfloatに変換
    geolocation = {'lat': float(query_geolocation.split(',')[0]), 'lng': float(query_geolocation.split(',')[1]),
                   'zoom': float(query_geolocation.split(',')[2])}
    try:
        restaurants = nearby_search_api(geolocation, cuisine)['places']
    except KeyError:
        saved_restaurants = []
    else:
        top_searches_restaurants = sorted(
            restaurants,
            key=lambda x: x.get('userRatingCount', 0),
            reverse=True
        )[:3]

        saved_restaurants = saving_restaurants(top_searches_restaurants)
    print(saved_restaurants)
    path = 'user_rating_count_searches'
    path_icon = select_path_icon(path)
    cuisine_icon = select_cuisine_icon(cuisine)
    template = loader.get_template('polls/user_rating_count_searches.html')
    context = {
        'front_maps_api_key': settings.FRONT_MAPS_API_KEY,
        'geolocation': geolocation,
        'cuisine': cuisine,
        'saved_restaurants': saved_restaurants,
        'path': path,
        'color': 'secondary',
        'path_icon': path_icon,
        'cuisine_icon': cuisine_icon,
    }
    return HttpResponse(template.render(context, request))


@login_required
def niche_searches(request, query_geolocation, cuisine):
    # 文字列をカンマで分割してfloatに変換
    geolocation = {'lat': float(query_geolocation.split(',')[0]), 'lng': float(query_geolocation.split(',')[1]),
                   'zoom': float(query_geolocation.split(',')[2])}
    try:
        restaurants = nearby_search_db(geolocation, cuisine)['places']
    except KeyError:
        saved_restaurants = []
    else:
        # restaurantsの中からdistanceが短い順に並べ替えて、最初の3つを取得
        top_searches_restaurants = sorted(
            restaurants,
            key=lambda x: x.get('distance', 0)
        )[:3]

        saved_restaurants = top_searches_restaurants
    print(saved_restaurants)
    path = 'niche_searches'
    path_icon = select_path_icon(path)
    cuisine_icon = select_cuisine_icon(cuisine)
    template = loader.get_template('polls/niche_searches.html')
    context = {
        'front_maps_api_key': settings.FRONT_MAPS_API_KEY,
        'geolocation': geolocation,
        'cuisine': cuisine,
        'saved_restaurants': saved_restaurants,
        'path': path,
        'color': 'success',
        'path_icon': path_icon,
        'cuisine_icon': cuisine_icon,
    }
    return HttpResponse(template.render(context, request))
