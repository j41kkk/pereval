
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0007_rename_beautytitle_perevaladded_beauty_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='perevalimages',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]