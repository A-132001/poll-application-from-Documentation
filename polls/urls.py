from . import views
from django.urls import path
app_name = 'polls'
urlpatterns =[
    path("",views.Questions,name="Questions_view"),
    path("<int:question_id>",views.question_detail,name="detail"),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/results/', views.results, name='results'),

]
