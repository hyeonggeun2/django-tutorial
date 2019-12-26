from django.urls import path
from .views import index, detail, results, vote, IndexView, DetailView
from . import views

app_name = 'polls'

urlpatterns = [
    path('', index, name='index'),
    path('<int:question_id>/', detail, name='detail'),
    path('<int:question_id>/results/', results, name='results'),
    path('<int:question_id>/vote/', vote, name='vote'),
    # 함수는 그냥 사용했지만 클래스는 as_view()를 이용해야 함
    path('cbv/', IndexView.as_view()),
    path('cbv/<int:pk>/', DetailView.as_view())
]