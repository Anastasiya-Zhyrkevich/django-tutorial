from django.urls import path 
from . import views

app_name = 'polls'
urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
  path('example', views.simple_example, name='simple_example'),
  path('<int:pk>/', views.DetailView.as_view(), name='detail'),
  path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
  path('<int:question_id>/vote/', views.votes, name='vote')
]
