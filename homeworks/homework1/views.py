import logging
from django.http import HttpResponse
# from django.shortcuts import render

# Create your views here.

logger = logging.getLogger(__name__)


def index(request):
    html = """
    <h1>Добро пожаловать на сайт</h1>
    <p>Здесь вы найдете информацию обо мне и моем проекте.</p>
    """
    logger.info('Index page accessed')
    return HttpResponse(html)


def about(request):
    html = """
    <h1>Обо мне</h1>
    <p>Здесь я расскажу о себе и своем первом Django проекте.</p>
    """
    logger.debug('About page accessed')
    return HttpResponse(html)
