
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0002_usertourist_perevaladded_add_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perevaladded',
            name='status',
            field=models.CharField(choices=[('new', 'new'), ('pending', 'pending'), ('accepted', 'accepted'), ('rejected', 'rejected')], default=('new', 'new'), max_length=50),
        ),
    ]