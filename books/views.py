from copy import copy
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from books.models import Book


class BookListView(ListView):
    template_name = "book_list.html"
    queryset = Book.objects.all().order_by('id')
    paginate_by = 2

    def get_context_data(self, *args, **kwargs):
        context = super(BookListView, self).get_context_data(*args, **kwargs)
        if 'page' in self.request.GET:
            request_clone = copy(self.request)
            request_clone.GET._mutable = True
            if len(request_clone.GET.getlist('page')) >= 1:
                del request_clone.GET['page']
            request_clone.GET._mutable = False
            context['request'] = request_clone
        return context


class BookDetailView(DetailView):
    template_name = "book_detail.html"
    queryset = Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        context['sold'] = self.object.bought_by.count()
        return context
