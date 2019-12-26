# class base view
from django.views import generic, View

from polls.models import Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class VoteView(View):
    def post(self, request, question_id):
        # post 요청만 받아서 실행해주면 됨
        pass