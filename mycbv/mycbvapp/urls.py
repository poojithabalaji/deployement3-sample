from django.urls import path
from mycbvapp.views import studentListView, studentDetailView, studentCreateView, studentUpdateView, studentDeleteView
from mycbvapp import views
urlpatterns=[
    path('',studentListView.as_view(), name='list'),
    path('create/',studentCreateView.as_view(), name='create'),
    path('<slug:pk>/',studentDetailView.as_view(),name='details'),
    path('update/<slug:pk>/',studentUpdateView.as_view(),name='update'),
    path('delete/<slug:pk>/',studentDeleteView.as_view(), name='delete'),
]
