"""
Django command to wait for the database to be available.
"""
from django.core.management.base import BaseComand


class Command(BaseComand):
    """Django command to wait for the database."""

    def handle(self, *args, **options):
        pass
