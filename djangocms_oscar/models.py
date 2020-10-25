from django.db import models

from cms.models import CMSPlugin


class FeaturedProduct(CMSPlugin):
    product = models.ForeignKey('catalogue.Product', on_delete=models.CASCADE)

    def __unicode__(self):
        return unicode(self.product)
