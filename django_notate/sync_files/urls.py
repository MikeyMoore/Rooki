from django.conf.urls import include, url
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings
# from django_notate.sync_files.views import list

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$',views.list, name='list'),
    url(r'^$', RedirectView.as_view(url='/sync_files/list/', permanent=True))
    # url(r'^current', views.current_datetime, name='current_datetime')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

