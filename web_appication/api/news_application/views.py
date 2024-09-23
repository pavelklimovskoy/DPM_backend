from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *


class AllNewsPage(APIView):
    """
    Отображение всех новостей
    """

    def get(self, request: WSGIRequest) -> render:
        news = NewsPost.objects.all()
        return render(request, 'news_application/index.html', {
            'debug': settings.DEBUG,
            'news': news
        }, status=200)


class NewsPage(APIView):
    """
    Получение новости по id
    """

    def get(self, request: WSGIRequest, newsId: int) -> render:
        try:
            news = NewsPost.objects.get(id=newsId)
            news.views_count += 1
            news.save()

            return render(request, 'news_application/current_news.html', {
                'debug': settings.DEBUG,
                'news': news
            }, status=200)

        except NewsPost.DoesNotExist as error:
            return Response(status=404)

# class CreateNews(APIView):
#     def post(self, request: WSGIRequest) -> Response | JsonResponse:
#         try:
#             serializer = CategorySerializers(data=request.data, many=False)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             else:
#                 return Response(status=status.HTTP_400_BAD_REQUEST)
#         except IntegrityError as error:
#             return JsonResponse(f'Category with name="{request.POST.get("category_name")}" already exist', safe=False)
