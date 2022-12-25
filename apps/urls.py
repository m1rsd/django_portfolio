from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from apps.views.views import IndexView, ProjectDetailView
from root import settings

urlpatterns = [
    path('', IndexView.as_view(), name='index_page'),
    path('project/<str:slug>', ProjectDetailView.as_view(), name='project_view'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
