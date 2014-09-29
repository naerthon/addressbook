from django.conf.urls import patterns, include, url
import contacts.views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', contacts.views.ListContactView.as_view(), name='contacts-list'),
    url(r'^new$', contacts.views.CreateContactView.as_view(),
        name='contacts-new'),
    url(r'^admin/', include(admin.site.urls)),
)
