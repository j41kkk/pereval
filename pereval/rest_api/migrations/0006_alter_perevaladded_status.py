from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0005_remove_perevaladded_raw_data_perevaladded_coords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perevaladded',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'New'), (2, 'Pending'), (3, 'Accepted'), (4, 'Rejected')], default=1),
        ),
    ]