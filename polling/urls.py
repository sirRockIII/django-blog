from django.urls import path
from . import views


urlpatterns = [
    path('', views.list_view, name="poll_index"),
    path('polls/<int:poll_id>/', views.detail_view, name="poll_detail"),
]