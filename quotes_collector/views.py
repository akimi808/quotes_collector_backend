from .models import Quote, Author, Source
from django.views.generic import View
from .utils import ObjectDetailMixin

from django.core import serializers
from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Quote
from .serializers import QuoteSerializer


def quotes_list(request):
    quotes = Quote.objects.all()
    serialized = serializers.serialize("json", quotes, indent=4)
    return HttpResponse(serialized, content_type='application/json')


def authors_list(request):
    authors = Author.objects.all()
    serialized = serializers.serialize("json", authors, indent=4)
    return HttpResponse(serialized, content_type='application/json')


def sources_list(request):
    sources = Source.objects.all()
    serialized = serializers.serialize("json", sources, indent=4)
    return HttpResponse(serialized, content_type='application/json')


def get_specific_quote(request, quote_id):
    quote = Quote.objects.get(pk=quote_id)
    serialized = serializers.serialize("json", [quote,], indent=4)
    return HttpResponse(serialized, content_type='application/json')


def get_quotes_by_author(request, author_id):
    authors_quotes = Quote.objects.filter(author=author_id)
    serialized = serializers.serialize("json", authors_quotes, indent=4)
    return HttpResponse(serialized, content_type='application/json')


def get_quotes_from_source(request, source_id):
    sources_quotes = Quote.objects.filter(source=source_id)
    serialized = serializers.serialize("json", sources_quotes, indent=4)
    return HttpResponse(serialized, content_type='application/json')


@csrf_exempt
def create_quote(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = QuoteSerializer(data=data)
        if serializer.is_valid():
            serializer.create(data) #нужно ли вызывать create?
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def quote_detail(request, quote_id):
    try:
        quote = Quote.objects.get(pk=quote_id)
    except Quote.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = QuoteSerializer(quote)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = QuoteSerializer(quote, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        quote.delete()
        return HttpResponse(status=204)


class QuoteDetail(ObjectDetailMixin, View):
    model = Quote