
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0003_alter_perevaladded_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerevalCoords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(blank=True, max_length=100, null=True)),
                ('longitude', models.CharField(blank=True, max_length=100, null=True)),
                ('height', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='perevaladded',
            name='height',
        ),
        migrations.RemoveField(
            model_name='perevaladded',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='perevaladded',
            name='longitude',
        ),
    ]