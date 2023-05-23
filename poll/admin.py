from django.contrib import admin

# Register your models here.
from .models import Question, Choice
#admin.site.register(Question)
#admin.site.register(Choice)

#class QuestionAdmin(admin.ModelAdmin):
#    fields = ['pub_date',"question_text"]
    ##field keyword is necssary
#admin.site.register(Question, QuestionAdmin)

class ChoiceInline(admin.TabularInline): #to show choices in row use StackedInline instead of TabularInline
    model = Choice
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    #to make filedset
    fieldsets = [
        (None, {"fields":["question_text"]}),
        ("date information",{"fields":["pub_date"],"classes":["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ['question_text', 'pub_date', 'was_published_recently']
admin.site.register(Question,QuestionAdmin)

#this is to show the lists of choices seperate
class ChoiceAdmin(admin.ModelAdmin):
    fields = ['votes', 'choice_text', 'question']
    #field keyword is necessary
admin.site.register(Choice, ChoiceAdmin)
