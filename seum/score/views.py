from django.shortcuts import render
from django.http import HttpResponse
from score.models import Book, Deadline
# Create your views here.
def index(request):
    context = dict()
    books = Book.objects.all()
    deadline = Deadline.objects.get(id=1)
    context["books"] = books
    context["deadline"] = deadline
    return render(request, 'score/index.html', context= context)

