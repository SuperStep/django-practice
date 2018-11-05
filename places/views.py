from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Category, Place

class IndexView(generic.ListView):
    template_name = 'places/index.html'
    context_object_name = 'latest_places_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Place.objects.order_by('-updated_at')[:5]

class DetailView(generic.DetailView):
    model = Place
    template_name = 'places/detail.html'