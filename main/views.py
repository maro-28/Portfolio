from django.views.generic import ListView, DetailView, TemplateView
from .models import Post, Comment, Category, SubCategory, Tag
from django.views.generic.edit import ModelFormMixin
from .forms import CommentCreateForm, PostSearchForm
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect


# ナビ用のコンテクスト
def get_navi_context_data(context):
    # 全てのカテゴリとサブカテゴリー
    context["category_list"] = Category.objects.all()
    context["subcategory_list"] = SubCategory.objects.all()

    # 検索フォーム
    global_form = PostSearchForm()
    context["global_form"] = global_form

    return context


# 記事の一覧のベース
class BaseListView(ListView):
    # 表示する記事の数
    paginate_by = 5

    # 作成日が新しい順にソート
    def get_queryset(self):
        queryset = Post.objects.order_by("-created_datetime").select_related("target_subcategory")
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # ナビ用のコンテクスト
        get_navi_context_data(context)
        return context


# 固定ページのベース
class BaseTemplateView(TemplateView):

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # ナビ用のコンテクスト
        get_navi_context_data(context)
        return context


# サイト紹介
class AboutBlogView(BaseTemplateView):
    template_name = 'main/about_blog.html'


# 自己紹介
class AboutMeView(BaseTemplateView):
    template_name = 'main/about_me.html'


# 最新記事一覧　検索による絞り込みの結果一覧
class TopView(BaseListView):

    # 検索ワードの読み込み
    def get_queryset(self):
        queryset = super().get_queryset()
        global_form = PostSearchForm(self.request.GET)
        global_form.is_valid()
        keyword = global_form.cleaned_data["keyword"]

        # 検索ワードがある場合
        if keyword:
            for word in keyword.split():
                queryset = queryset.filter(
                    Q(title__icontains=word) | Q(main_sentence__contains=word)
                )
            return queryset

        # 検索ワードがない場合
        else:
            return queryset


# 記事の詳細
class PostDetailView(ModelFormMixin, DetailView):
    model = Post
    form_class = CommentCreateForm
    template_name = "main/post_detail.html"

    # コメントの登録
    def form_valid(self, form):
        post_pk = self.kwargs["pk"]
        comment = form.save(commit=False)
        comment.post = get_object_or_404(Post, id=post_pk)
        comment.save()
        return redirect("main:post_detail", pk=post_pk)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            self.object = self.get_object()
            return self.form_invalid(form)

    # templateにcategory_list, subcategory_list, global_form, r_post_listを返す
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)

        get_navi_context_data(context)

        # 関連記事
        post_pk = self.kwargs["pk"]
        tar_post = Post.objects.get(id=post_pk)
        tar_tags = tar_post.tag
        tar_sub = tar_post.target_subcategory

        # 同じタグの作成日が新しい順
        filtered_posts = Post.objects.order_by("-created_datetime").filter(
            tag__in=[tag for tag in tar_tags.all()]).exclude(id=post_pk)

        # コメント
        context["comment_list"] = Comment.objects.filter(post=tar_post).order_by("-created_datetime")

        # 3記事以上あるか
        if len(filtered_posts) >= 3:
            context["r_post_list"] = filtered_posts[:3]

        # 無ければ同じサブカテゴリーも含む
        else:
            context["r_post_list"] = Post.objects.order_by("-created_datetime").filter(
                Q(tag__in=[tag for tag in tar_tags.all()]) | Q(target_subcategory=tar_sub)
            ).exclude(id=post_pk)[:3]
        return context


# サブカテゴリーでソート
class SubCategoryView(BaseListView):

    # サブカテゴリーの読み込み
    def get_queryset(self):
        subcategory_name = self.kwargs["subcategory"]
        self.target_subcategory = SubCategory.objects.get(name=subcategory_name)
        queryset = super().get_queryset().filter(target_subcategory=self.target_subcategory)
        return queryset

    # templateにsubcategoryを返す
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["subcategory"] = self.target_subcategory
        return context


# タグでソート
class TagView(BaseListView):
    # タグの読み込み
    def get_queryset(self):
        tag_name = self.kwargs["t"]
        self.tag = Tag.objects.get(name=tag_name)
        queryset = super().get_queryset().filter(tag=self.tag)
        return queryset

    # templateにtagを返す
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["tag"] = self.tag
        return context
