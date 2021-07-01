from django.urls import path
#from . import views
from .views import AddPost, ArticleView, HomeView, UpdateArticleView, DeleteArticleView
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleView.as_view(), name = "article"),
    path('add', AddPost.as_view(), name = "add_post"),
    path('article/edit/<int:pk>', UpdateArticleView.as_view(), name = "update"),
    path('article/<int:pk>/delete', DeleteArticleView.as_view(), name = "delete"),
]