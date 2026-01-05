from django.core.management.base import BaseCommand
from dataentry.models import Student

class Command(BaseCommand):
    help = "It will insert data to the database"

    def handle(self, *args, **kwargs):

        dataset = [
            {'roll_no': 1002, 'name': 'Sachin', 'age': 25},
            {'roll_no': 1003, 'name': 'Rushi', 'age': 27},
            {'roll_no': 1004, 'name': 'Manish', 'age': 28},
            {'roll_no': 1005, 'name': 'Mayur', 'age': 29},
        ]

        for data in dataset:
            roll_no = data['roll_no']
            exists = Student.objects.filter(roll_no = roll_no).exists()
            if not exists:
                Student.objects.create(roll_no = data['roll_no'], name = data['name'], age = data['age'])
                self.stdout.write(self.style.SUCCESS('Data Inserted Successfully'))
            else:
                self.stdout.write(self.style.WARNING('Student Already Exists.'))

        # Student.objects.create(roll_no = '182029', name='Kedar', age = 26)
        