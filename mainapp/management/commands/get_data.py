from django.core.management.base import BaseCommand, CommandError
import sys, os, shutil
import csv
import json
from mainapp.models import User


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str)

    def csv_reader(self, file):
        with open(file, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                    continue
                data = dict(row)
                User.objects.get_or_create(data=data)
                line_count += 1

    def handle(self, *args, **options):
        lists_file = options['file']
        print(lists_file)
        self.csv_reader(lists_file)
        print('Finished')
