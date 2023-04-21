
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTourist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phone', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=255)),
                ('first_name', models.CharField(blank=True, max_length=155)),
                ('last_name', models.CharField(blank=True, max_length=155)),
            ],
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='add_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='autumn',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Осень'),
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='beautyTitle',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='connect',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='date_added',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='height',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='latitude',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='longitude',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='other_titles',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='pereval_areas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rest_api.perevalareas'),
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='raw_data',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='spring',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Весна'),
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='status',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='summer',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Лето'),
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='winter',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Зима'),
        ),
        migrations.AddField(
            model_name='perevalimages',
            name='date',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rest_api.perevaladded'),
        ),
        migrations.AddField(
            model_name='perevalimages',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='perevalareas',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rest_api.perevalareas'),
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='user_tourist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rest_api.usertourist'),
        ),
    ]