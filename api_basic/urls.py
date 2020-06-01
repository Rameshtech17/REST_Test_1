from django.urls import path
from .views import article_list, article_details
# from .views import ArticlAPIView, ArticleAPIDetails


urlpatterns = [
    path('article/', article_list),
    path('detail/<int:pk>', article_details),

    # path('article/', ArticleAPIView.as_view()),
    # path('details/<int:id>', ArticleAPIDetails.as_view()),


]
