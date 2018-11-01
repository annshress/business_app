from sys import stdout

from django.core.management import BaseCommand
from django.db import DEFAULT_DB_ALIAS
from django.apps import apps as global_apps

from books.factory import PublisherFactory, BookFactory, AayuUserFactory


class Command(BaseCommand):
    help = "Initializes database with dummy data."
    books = 5
    users = 2
    publishers = 3

    def add_arguments(self, parser):
        parser.add_argument(
            'books', nargs='?',
            help='Books you want to create. Default: %d' % self.books,
        )
        parser.add_argument(
            'users', nargs='?',
            help='Users you want to create. Default: %d' % self.users,
        )
        parser.add_argument(
            'publishers', nargs='?',
            help='Publishers you want to create. Default: %d' % self.publishers,
        )

    def handle(self, *args, **options):
        books = options['books'] or self.books
        users = options['users'] or self.users
        publishers = options['publishers'] or self.publishers

        # app_config = args[0] if args else None
        # using = options.get("using", DEFAULT_DB_ALIAS)
        apps = options.get("apps", global_apps)

        try:
            apps.get_model('books', 'Book')
            apps.get_model('books', 'Publisher')
            AayuUser = apps.get_model('users', 'AayuUser')
        except LookupError:
            stdout.write("Models aren't loaded yet.")
            return

        if AayuUser.objects.last():
            AayuUserFactory.reset_sequence(AayuUser.objects.last().id + 1)

        pubs = PublisherFactory.create_batch(publishers)
        boks = []
        for each in range(books):
            boks.append(BookFactory.create(publisher=pubs[each % publishers]))
        usrs = AayuUserFactory.create_batch(users)

        for u in range(users):
            usrs[u].books_bought.add(*boks[:u+1])

        stdout.write(f'{books} Book(s), '
                     f'{publishers} Publication(s), '
                     f'{users} User(s) successfully created.')
