from django.shortcuts import render,get_object_or_404
from . import models
from django.http import HttpResponse ,HttpResponseRedirect
from django.urls import reverse

# def firstview(request):
#     return HttpResponse("Hello World")

def Questions(request):
    question_list = models.Question.objects.order_by("-pub_time")[:5]
    # output = ','.join([q.question_text for q in question_list])
    return render(request,"polls/questions.html",{"latest_question_list":question_list})

def question_detail(request,question_id):
    question = get_object_or_404(models.Question,pk=question_id)
    return render(request,'polls/detail.html',{"question":question})


def vote(request, question_id):
    question = get_object_or_404(models.Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, models.Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    

def results(request,question_id):
    result = get_object_or_404(models.Question,pk=question_id)
    return render(request,"polls/results.html",{"question":result})