from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return [
            'website:index',
            'website:contact_us',
            'website:product_list',
            'website:capsule',
            'website:rotary',
            'website:blog_list',
            'website:create_blog_post',
            'website:view_blog_post',
        ]

    def location(self, item):
        return reverse(item)
