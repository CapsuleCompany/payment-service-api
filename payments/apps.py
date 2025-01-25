from django.apps import AppConfig
from django.db.models.signals import pre_migrate
from django.db import connection


class PaymentsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "payments"

    def ready(self):
        pre_migrate.connect(create_schema, sender=self)

def create_schema(sender, **kwargs):
    schema_name = "payment_api"
    with connection.cursor() as cursor:
        cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {schema_name};")
