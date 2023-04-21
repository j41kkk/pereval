
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0004_perevalcoords_remove_perevaladded_height_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perevaladded',
            name='raw_data',
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='coords',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rest_api.perevalcoords'),
        ),
    ]