from django.contrib import admin
from chinese.models import Product, ContactMessage, BlogPost

# Register your models here.
admin.site.register(Product),
admin.site.register(ContactMessage),
admin.site.register(BlogPost),
