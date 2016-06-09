from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse


from .models import Question,Choice

def indexold(request ):
    context=["anc","dfads ","dadff "]
    return render(request,'indexold.html',{'context':context})


def index(request):
     latest_question_list = Question.objects.all()
     output= ','.join([q.context for q in latest_question_list])
     return HttpResponse(output)


#def results(request, question_id):
#    response = "You're looking at the results of question %s."
#    return HttpResponse(response % question_id)
#

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'detail.html', {
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


#def vote(request,question_id):
#	question =get_object_or_404(Question,pk=question_id)
#	try:
#		select_choice= question.choice_set.get(pk=request.POST['choice'])
#
#	except (KeyError,Choice.DoesNotExist):
#		return render(request,'polls/detail.html',{
#			'question':question,
#			'error_msg':"you didn't select a choice",
#			})
#		
#	else:
#		select_choice.votes +=1
#		select_choice.save()
#                return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
#

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'detail.html', {'question': question})


## Create your views here.
#def index(req):
#    question_list=Question.objects.all()
#    return render(request,"polls/index.html",{"question_list":question_list},
#)
##def index(request):
##    question_list = Question.objects.all()
##
##    return render(
##        request,
##        "polls/index.html",
##        {'question_list': question_list},
##    )
#    
#
#def add_done(request):
#    add_question = Question()
#    content = request.POST['content']
#    add_question.context = content
#    add_question.save()
#    return render(
#        request,
#        "polls/add_done.html",
#        {'question': content},
#
#
#    )
#
#
#def add(request):
#    return render(request, "polls/add.html")
