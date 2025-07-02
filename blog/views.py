from rest_framework.viewsets import ViewSet
from .models import Blog
from .serializers import AllBlogSerializer, BlogDetailSerializer
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.utils.translation import gettext_lazy as _


class BlogViewSet(ViewSet):
    @swagger_auto_schema(
        operation_description="Get All Blogs",
        operation_summary="Get All Blogs",
        responses={
            200: AllBlogSerializer(),
        },
        tags=['blog']
    )
    def get_all(self, request, *args, **kwargs):
        blogs = Blog.objects.all()
        serializer = AllBlogSerializer(blogs, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Get Blog By Id",
        operation_summary="Get Blog By Id",
        responses={
            200: BlogDetailSerializer(),
        },
        tags=['blog']
    )
    def get_by_id(self, request, *args, **kwargs):
        blog = Blog.objects.filter(id=kwargs['pk']).first()
        if blog is None:
            return Response(data={'error': _('Content not found')}, status=status.HTTP_404_NOT_FOUND)
        blog.view_count += 1
        blog.save(update_fields=['view_count'])
        serializer = BlogDetailSerializer(blog, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)