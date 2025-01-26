from django.urls import path
from . import views
urlpatterns=[
path ("blogposts/",views.BlogPostListCreate.as_view(), name="blogpost-view-create"),# .as_view() means anytime we go to the route we will go to that page and interact with the api
path("blogposts/<int:pk>/",views.BlogPostRetrieveUpdateDestroy.as_view(), name='update'),
path("blogposts/", views.BlogPostList.as_view(), name='title'),


]