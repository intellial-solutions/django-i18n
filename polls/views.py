from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
# from django.utils import translation

# Create your views here.
def index(request):
    # translation.activate("nl")
    # quote = _("Hello, world. You're at the polls index.")
    # quote = quote + ". <a href='/polls/page/'>Page</a>"
    # return HttpResponse(quote)

    return render(request, 'polls/index.html', {})

def page(request):
    # translation.activate("de")
    # return render(request, 'polls/page.html', {})
    page_text = _("This is HTML translation.")
    return HttpResponse(page_text)

def lang(request):
    return render(request, 'polls/lang.html', {})