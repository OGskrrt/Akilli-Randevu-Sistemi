from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from mainapp.models import Sifreler

class Command(BaseCommand):
    help = 'Migrates data from Sifreler table to Django User model'

    def handle(self, *args, **kwargs):
        for sifreler in Sifreler.objects.all():
            user, created = User.objects.get_or_create(username=sifreler.user_id)
            user.set_password(sifreler.password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully migrated user {user.username}'))
