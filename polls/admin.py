from django.contrib import admin

from .models import Question, Choice


# StackedInline(구체적이고 길어보이는 테이블) VS TabularInline(간결하고 짧은 테이블)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    # 모양을 정하는데, 첫번째 인자는 필드셋의 이름을 나타냄
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        # 'classes' ['collapse'] 설정을 추가하면 감추기, 보기가 나옴
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    # 리스트 화면을 어떻게 보여줄 지 정함
    list_display = ('question_text', 'pub_date', 'was_published_recently')
