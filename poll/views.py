from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.views import generic
from django.utils import timezone

def index(request):
    #making questions with publishing date in future invisible
    latest_question_list = Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:6]
    context = { "latest_question_list": latest_question_list}
    return render(request, "ind_template.html", context)

def details(request, question_id):
    short = get_object_or_404(Question, pk = question_id)
    return render(request, "det_template.html", {'question':short})    

def vote(request, question_id):
    #return HttpResponse("you are voting on Question %s" ,question_id)
    question = get_object_or_404(Question, pk = question_id)
    try:
        sel_choice = question.choice_set.get(pk = request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, "det_template.html", {'question':question, "err_message":"You did not selected any choice"},)
    else:
        sel_choice.votes = sel_choice.votes + 1
        sel_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button
        return HttpResponseRedirect(reverse("polling_app:results",  args = (question.id,)))
    
def results(request, question_id):
    #re = "You're looking the at the result of question %s"
    #return HttpResponse(re ,question_id)
    quest = get_object_or_404(Question, pk = question_id)
    return render(request ,"res_template.html", {'question':quest})













