from django.urls import path
from chinese import views
from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('about-us/', views.about_us, name='about_us'),
    path('product_list/', views.product_list, name='product_list'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/create/', views.create_blog_post, name='create_blog_post'),
    path('blog/<int:post_id>/', views.view_blog_post, name='view_blog_post'),



]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
