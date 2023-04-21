
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0009_rename_date_perevalimages_data_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perevalimages',
            name='data_img',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image', to='rest_api.perevaladded'),
        ),
    ]