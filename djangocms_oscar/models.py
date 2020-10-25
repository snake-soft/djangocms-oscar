from django.db import models

from cms.models import CMSPlugin, fields


class FeaturedProduct(CMSPlugin):
    product = models.ForeignKey('catalogue.Product', on_delete=models.CASCADE)


def get_slotname(instance):
    return



#===============================================================================
# class MyModel(models.Model):
#     # your fields
#     my_placeholder = fields.PlaceholderField('placeholder_name')
#===============================================================================
