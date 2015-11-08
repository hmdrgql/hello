from django.conf.urls import patterns, include, url
from django.contrib import admin
from books.views import search_form
from books.views import search_results
from books.views import information
from books.views import delete
from books.views import renew
from books.views import new
urlpatterns = patterns('',
    # ...
    (r'^search_form/$', search_form),
    (r'^search_results/$', search_results),
    (r'^information/$',information),
    (r'^delete/$',delete),
    (r'^renew/$',renew),
    (r'^new/$',new),
    # ...
)
