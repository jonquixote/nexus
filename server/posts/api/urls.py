from .views import postAPIView
from django.conf.urls import url
urlpatterns = [
  url(r'^$', postAPIView.as_view(), name='post-create'),
]