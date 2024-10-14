# Create your views here.
from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.shortcuts import get_object_or_404
from django.conf import settings


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


def map(request):
    template = loader.get_template('polls/map_index.html')
    context = {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    return HttpResponse(template.render(context, request))

def near_by_searches(request):
    template = loader.get_template('polls/near_by_searches.html')
    context = {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    return HttpResponse(template.render(context, request))