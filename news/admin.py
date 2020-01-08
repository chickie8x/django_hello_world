from django.contrib import admin
from news.models import Category, Article
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin


admin.site.register(Category)
#admin.site.register(Article)


class ArticleResouces(resources.ModelResource):

    class Meta:
        model = Article
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields = ('article_feature_img', 'article_title', 'article_desc', 'article_content','article_category', 'published_date',)


class ArticleAdmin(ImportExportActionModelAdmin):
    resource_class = ArticleResouces


admin.site.register(Article, ArticleAdmin)
