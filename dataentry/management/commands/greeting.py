from django.core.management.base import BaseCommand

class Command(BaseCommand):

    help = "Greets the User"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Specifies User Name')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        greeting = f'Hi {name}, Good Morning!'
        self.stdout.write(greeting)
        self.stderr.write(greeting)
        self.stderr.write(self.style.SUCCESS(greeting))
