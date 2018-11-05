from copy import copy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from users.filters import UserFilter
from users.models import AayuUser as User


class UsersListView(ListView):
    template_name = "user_list.html"
    queryset = User.objects.all().order_by('id')
    paginate_by = 2

    def get_queryset(self):
        return UserFilter(
            data=self.request.GET,
            queryset=super(UsersListView, self).get_queryset()
        ).qs

    def get_context_data(self, *args, **kwargs):
        context = super(UsersListView, self).get_context_data(*args, **kwargs)
        context['filter'] = UserFilter(data=self.request.GET)
        context['ordering_a'] = self.request.GET.get('ordering_a')
        # context['ordering_b'] = self.request.GET.get('ordering_b')
        if 'page' in self.request.GET:
            request_clone = copy(self.request)
            request_clone.GET._mutable = True
            if len(request_clone.GET.getlist('page')) >= 1:
                del request_clone.GET['page']
            request_clone.GET._mutable = False
            context['request'] = request_clone
        return context


class UserDetailView(DetailView):
    template_name = "user_detail.html"
    queryset = User.objects.all()
