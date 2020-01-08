from django.db import models


class Category(models.Model):
    cat_name = models.CharField(max_length=500)

    def __str__(self):
        return self.cat_name


class Article(models.Model):
    article_feature_img = models.CharField(max_length=1000)
    article_title = models.CharField(max_length=1000)
    article_desc = models.TextField()
    article_content = models.TextField()
    article_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published_date = models.DateField()

    def __str__(self):
        return self.article_title
