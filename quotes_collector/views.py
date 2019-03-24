from .models import Quote, Author, Source
from django.views.generic import View
from .utils import ObjectDetailMixin

from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

from .models import Quote


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

#
# def create_quote(request):
#     quote = Quote.objects.create(text=text, author=author, source=source)



# def understand_what_user_wants(request_from_app):
#     user_wants = get_type_of_request(request_from_app)
#     if user_wants == 'save_quote':
#         save_qoute_to_db(request_from_app)
#     elif user_wants == "delete_all_quotes":
#         delete_all_quotes_from_db(request_from_app)
#     elif user_wants == 'delete_specific_quote':
#         delete_quote_from_db(request_from_app)
#     elif user_wants == 'delete_all_qoutes_from_book':
#         delete_all_qoutes_from_book(request_from_app)
#     elif user_wants == 'delete_all_qoutes_by_author':
#         delete_all_qoutes_by_author(request_from_app)
#     elif user_wants == 'fix_quote_text':
#         fix_quote_text(request_from_app)
#     elif user_wants == 'fix_book_title':
#         fix_book_title(request_from_app)
#     elif user_wants == 'fix_author_name':
#         fix_author_name(request_from_app)
#     else:
#         send_error_messge



class QuoteDetail(ObjectDetailMixin, View):
    model = Quote