from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from steganography.views import EmbedImageCreateView, ExtractImageCreateView, EmbedDetailsView, ExtractDetailsView, EmbedView, ExtractView

urlpatterns = {
    url(r'^api/embed-image/$', EmbedImageCreateView.as_view(), name="embed-image"),
    url(r'^api/extract-image/$', ExtractImageCreateView.as_view(), name="extract-image"),
    url(r'^api/embed-image/(?P<resource_uuid>[^/]+)/$', EmbedDetailsView.as_view(), name="embed-details"),
    url(r'^api/extract-image/(?P<resource_uuid>[^/]+)/$', ExtractDetailsView.as_view(), name="extract-details"),
    url(r'^embed/', EmbedView.as_view(), name="embed"),
    url(r'^extract/', ExtractView.as_view(), name="extract"),
}

urlpatterns = format_suffix_patterns(urlpatterns)