from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    # 最新記事一覧　検索による絞り込みの結果一覧
    path("", views.TopView.as_view(), name="top"),
    # ブログの紹介
    path("about_blog/", views.AboutBlogView.as_view(), name="about_blog"),
    # 自分について
    path("about_me/", views.AboutMeView.as_view(), name="about_me"),
    # 記事の詳細
    path("post_detail/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    # サブカテゴリーによる絞り込みの結果一覧
    path("subcategory/<str:subcategory>/", views.SubCategoryView.as_view(), name="subcategory"),
    # タグによる絞り込みの結果一覧
    path("tag/<str:t>/", views.TagView.as_view(), name="tag"),
]
