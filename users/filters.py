import django_filters as filters

from users.models import AayuUser as User


class UserFilter(filters.FilterSet):
    ordering_a = filters.OrderingFilter(
        fields=(
            ('username', 'a'),
            ('date_joined', 'b'),
        )
    )

    # ordering_b = filters.OrderingFilter(
    #     fields=(
    #         ('date_joined', 'b'),
    #     )
    # )

    class Meta:
        model = User
        fields = {
            'username': ['icontains']
        }
