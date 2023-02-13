from django.urls import path
from .import views


urlpatterns=[
    path('', views.HomeListView.as_view(), name='index'),
    path('browse/', views.BrowseListView.as_view(), name='browse'),
    path('details/', views.DetailsListView.as_view(), name='details'),
    path('streams/', views.StreamsListView.as_view(), name='streams'),
    path('profile/', views.ProfilListView.as_view(), name='profile')
]