from django.shortcuts import get_object_or_404, render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect 

from django.template import loader

from django.urls import path, reverse

from django.views import generic

from . import views

from .models import Movie

from .forms import MovieForm

from django.contrib import messages


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_movie_list'

    def get_queryset(self): 
        return Movie.objects.all().filter(score__gt=0).order_by('-pub_date')[:5]

class ToVoteView(generic.ListView):
    template_name = 'polls/to_vote.html'
    context_object_name = 'latest_movie_list'

    def get_queryset(self): 
        return Movie.objects.all().filter(score=0).order_by('-pub_date')

class DetailView(generic.DetailView):
    model = Movie
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Movie 
    template_name = 'polls/results.html'

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
        return HttpResponseRedirect('/polls/')

def add_entry(request):
    if request.method == 'POST': 
        form = MovieForm(request.POST)
        if form.is_valid() and form.cleaned_data['movie_text'] not in [str(i) for i in list(Movie.objects.all())]:
            form.save()
            new_movie = Movie.objects.all()[len(Movie.objects.all())-1]
            for i in range(1,6, 1):
                new_movie.choice_set.create(choice_text =str(i), votes = 0)
            return HttpResponseRedirect('/polls/')
        else: 
            messages.error(request, 'Movie already listed!')
    else: 
        form = MovieForm()
    context = {'form': form}
    return render(request, 'polls/new_topic.html', context)