from django.urls import path

from users.views import UsersListView, UserDetailView

urlpatterns = [
    path('', UsersListView.as_view(), name='list'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail'),
]
