
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0008_perevalimages_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perevalimages',
            old_name='date',
            new_name='data_img',
        ),
    ]