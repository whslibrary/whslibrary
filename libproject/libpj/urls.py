from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),

    path('upload', views.upload, name='upload'),
    path('upload_', views.upload_, name='upload_'),

    path('library', views.library, name='library'),
    path('search', views.book_search, name='book_search'),
    path('book_showcase', views.book_showcase, name='book_showcase'),

]

urlpatterns = format_suffix_patterns(urlpatterns)