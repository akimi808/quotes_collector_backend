from django.shortcuts import render
from .models import Quote
from django.views.generic import View
from .utils import ObjectDetailMixin
from django.db.models import Q

def quotes_list(request):
    #search_query = request.GET.get('search', '')
    quotes = Quote.objects.all()
    return render(request, 'index.html', context={'quotes' : quotes})


class QuoteDetail(ObjectDetailMixin, View):
    model = Quote
    template = 'quote_detail.html'
