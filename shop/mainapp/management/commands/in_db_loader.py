from django.core.management.base import BaseCommand
from mainapp.models import Category, Product
from shop.settings import STATICFILES_DIRS
import os, json

def json_loader(file_name):
    with open(os.path.join(STATICFILES_DIRS[0], file_name + '.json'), 'r', encoding='utf8') as infile:
        return json.load(infile)



class Command(BaseCommand):
    help = 'In db loader'

    def handle(self, *args, **options):
        categories = json_loader('new_categories')

        for category in categories:
            new_category = Category(**category)
            new_category.save()
            print('new_category added')