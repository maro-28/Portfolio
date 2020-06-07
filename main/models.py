from django.db import models

# Create your models here.

# カテゴリー
class Category(models.Model):
    # 名前
    name = models.CharField(max_length=20)

    # 作成日
    created_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# サブカテゴリー
class SubCategory(models.Model):
    # 名前
    name = models.CharField(max_length=20)

    # 作成日
    created_datetime = models.DateTimeField(auto_now_add=True)

    # 親カテゴリー
    target_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# タグ
class Tag(models.Model):
    # 名前
    name = models.CharField(max_length=50)

    #作成日
    created_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# 記事
class Post(models.Model):
    # タイトル
    title = models.CharField(max_length=100)

    # テキスト
    main_sentence = models.TextField(blank=True)

    # 作成日と更新日
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    # サブカテゴリー
    target_subcategory = models.ForeignKey(SubCategory, null=True, blank=True, on_delete=models.CASCADE)

    # タグ
    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title


# コメント
class Comment(models.Model):
    # 投稿者の名前
    name = models.CharField("Name" ,max_length=50)

    # 年齢
    age = models.PositiveSmallIntegerField("Age", default=25)

    # 性別の選択肢
    SEX_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
    )

    # 性別
    sex = models.CharField("Sex", max_length=6, choices=SEX_CHOICES, default="Male")

    # 内容
    text = models.TextField("Content")

    # 作成日
    created_datetime = models.DateTimeField("作成日",auto_now_add=True)

    # どの記事についてか
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="対象記事", null=True)

    # 返信
    reply = models.TextField("返信内容", default="まだ返信がありません。")

    def __str__(self):
        return self.text[:20]
