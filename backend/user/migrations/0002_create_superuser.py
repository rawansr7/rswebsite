from ..models import User
from django.db import migrations
from django.conf import settings


def createsuperuser(apps, schema_editor) -> None:
    """
    Dynamically create an admin user as part of a migration
    """

    User.objects.create_superuser(
        settings.SUPERUSER_USERNAME, password=settings.SUPERUSER_PASSWORD
    )
    User.objects.create_user(
        username="hasankassim7@hotmail.com",
        email="hasankassim7@hotmail.com",
        password="12345678",
        first_name="Hasan",
        last_name="Kassem",
    )


class Migration(migrations.Migration):

    initial = True
    dependencies = [
        ("user", "0001_initial"),
    ]
    operations = [migrations.RunPython(createsuperuser)]
