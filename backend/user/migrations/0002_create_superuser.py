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


class Migration(migrations.Migration):

    initial = True
    dependencies = [
        ("user", "0001_initial"),
    ]
    operations = [migrations.RunPython(createsuperuser)]
