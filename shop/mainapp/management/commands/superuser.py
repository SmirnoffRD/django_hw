from django.core.management.base import BaseCommand
from authapp.models import Custom_User

class Command(BaseCommand):
    help = 'superuser'

    def handle(self, *args, **options):
        name = input("Name: ")
        _password = input("Password: ")
        email = input("E-mail: ")
        _age = int(input("Age: "))
        super_user = Custom_User.objects.create_superuser(username=name, email=email, password=_password, age=_age)
        super_user.save()
        print("super_user added")
        