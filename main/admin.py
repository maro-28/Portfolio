from django.contrib import admin
from .models import Post, Comment, Category, SubCategory, Tag

# 記事
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', "target_subcategory", "tags",  'created_datetime', 'updated_datetime', 'id')
    list_display_links = ('title', "target_subcategory", "tags",  'created_datetime', 'updated_datetime', 'id',)

    # タグをすべて表示
    def tags(self, row):
        return " ".join([x.name for x in row.tag.all()])

# コメント
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "name", "created_datetime", "sex", "age", "text", "reply")
    list_display_links = ("post", "name",  "sex", "age", "created_datetime")

# カテゴリー
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_datetime")
    list_display_links = ("name", "created_datetime")

# サブカテゴリー
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "target_category",  "created_datetime")
    list_display_links = ("name", "target_category",  "created_datetime")

# タグ
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "created_datetime")
    list_display_links = ("name", "created_datetime")

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Tag, TagAdmin)
