from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>/', views.category, name='category')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)