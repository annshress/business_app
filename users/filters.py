import django_filters as filters

from users.models import AayuUser as User


class UserFilter(filters.FilterSet):
    o = filters.OrderingFilter(
        fields=(
            ('username', 'a'),
            ('name', 'b'),
            ('is_active', 'c'),
            ('age', 'd'),
        )
    )

    class Meta:
        model = User
        fields = {
            'username': ['icontains']
        }
