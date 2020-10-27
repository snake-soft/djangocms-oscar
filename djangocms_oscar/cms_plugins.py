from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import FeaturedProduct


class FeaturedProductPlugin(CMSPluginBase):
    model = FeaturedProduct
    name = _("Featured product")
    admin_preview = True
    render_template = 'djangocms_oscar/plugins/product.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


class SearchFormPlugin(CMSPluginBase):
    name = _("Search Form")
    admin_preview = True
    render_template = 'djangocms_oscar/plugins/search_form.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


plugin_pool.register_plugin(FeaturedProductPlugin)
plugin_pool.register_plugin(SearchFormPlugin)
