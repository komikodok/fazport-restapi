from django.urls import path
from .views import ProjectListView, ProjectDetailView

urlpatterns = [
    path('', ProjectListView.as_view()),
    path('<str:slug>/', ProjectDetailView.as_view())
]
