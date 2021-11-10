
from django.contrib import admin
from django.urls import include, path

from pages.views import home_view, contact_view, about_view


urlpatterns = [
    path('blog/', include('blog.urls')),
    path('courses/', include('courses.urls')),
    path('products/', include('products.urls')),
    path('', home_view, name='home'),
    path('about/<int:id>/', about_view, name='product-detail'),
    path('contact/', contact_view),
    path('admin/', admin.site.urls),
]
