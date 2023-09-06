from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Writer(models.Model):
    name = models.CharField(max_length=30)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.name


class Publication(models.Model):
    name = models.CharField(max_length=20)
    writers = GenericRelation(Writer, related_query_name='mywriters')

    def __str__(self):
        return self.name
