from django.shortcuts import get_object_or_404, render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect 

from django.template import loader

from django.urls import path, reverse

from . import views

from .models import Movie

from .forms import MovieForm


def index(request):
    latest_movie_list = Movie.objects.order_by('-score')[:5]
    context = {'latest_movie_list': latest_movie_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    movie = get_object_or_404(Movie, pk=question_id)
    return render(request, 'polls/detail.html', {'movie': movie})

def results(request, question_id):
    question = get_object_or_404(Movie, pk=question_id)
    return render(request, 'polls/results.html', {'movie': question})

def vote(request, question_id):
    question = get_object_or_404(Movie, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        m = Movie.objects.get(pk=question_id)
        m.score += int(selected_choice.choice_text)* selected_choice.votes
        m.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def add_entry(request):
	if request.method != 'POST': 
		# No data submitted; create a blank form. 
		form = MovieForm()
	else: 
		form = MovieForm(request.POST)
		if form.is_valid():
			form.save()
			new_movie = Movie.objects.all()[len(Movie.objects.all())-1]
			for i in range(1,6, 1):
				new_movie.choice_set.create(choice_text =str(i), votes = 0)
			return HttpResponseRedirect(reverse('polls:index'))

	context = {'form': form}
	return render(request, 'polls/new_topic.html', context)