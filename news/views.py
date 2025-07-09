from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .models import News
from .serializers import NewsSerializer, GetNewsSerializer
from django.utils.translation import gettext_lazy as _
from drf_yasg.utils import swagger_auto_schema


class NewsViewSet(ViewSet):
    @swagger_auto_schema(
        operation_description="Get News",
        operation_summary="Get News",
        responses={
            200: NewsSerializer(),
        },
        tags=['news']
    )
    def get_news(self, request, *args, **kwargs):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Get News By Id",
        operation_summary="Get News By Id",
        responses={
            200: GetNewsSerializer(),
        },
        tags=['news']
    )
    def get_news_by_id(self, request, *args, **kwargs):
        news = News.objects.filter(id=kwargs['pk']).first()
        if news is None:
            return Response(data={'error': _('News not found')}, status=status.HTTP_404_NOT_FOUND)
        news.view_count += 1
        news.save(update_fields=['view_count'])
        serializer = GetNewsSerializer(news, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)
