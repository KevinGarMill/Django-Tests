from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def mainpage(request):
    page = """
    <html>
        <body>
            Sobres, a PP Application.
        </body>
    </html>
    """

    return HttpResponse(page)
