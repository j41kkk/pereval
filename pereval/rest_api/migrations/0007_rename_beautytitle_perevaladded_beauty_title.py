
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0006_alter_perevaladded_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perevaladded',
            old_name='beautyTitle',
            new_name='beauty_title',
        ),
    ]