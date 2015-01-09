from autoslug import AutoSlugField
from django.db import models
from klingon.models import AutomaticTranslation


class Category(models.Model, AutomaticTranslation):
    name = models.CharField(max_length=100)
    description = models.TextField()
    #klingon begin
    translatable_fields = ('name', 'description')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Rant(models.Model, AutomaticTranslation):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = AutoSlugField(populate_from='title')
    # klingon begin
    translatable_fields = ('title', 'description', 'slug')
    translatable_slug = 'slug'

    def __str__(self):
        return self.title


