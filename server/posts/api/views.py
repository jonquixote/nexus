from rest_framework import generics, mixins
from posts.models import Post
from .serializers import  postSerializer
class postAPIView(mixins.CreateModelMixin, generics.ListAPIView):
  resource_name = 'posts'
  serializer_class = postSerializer
  serializer_class = postSerializer
  def get_queryset(self):
    return Post.objects.all()
  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)