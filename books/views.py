from django.core.paginator import Paginator
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from books.models import Book


class BookListView(ListView):
    template_name = "book_list.html"
    queryset = Book.objects.all().order_by('id')
    paginate_by = 2


class BookDetailView(DetailView):
    template_name = "book_detail.html"
    queryset = Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        context['sold'] = self.object.bought_by.count()
        return context
