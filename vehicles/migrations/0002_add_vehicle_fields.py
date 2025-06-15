# Generated migration for new vehicle fields

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lostvehicle',
            name='year',
            field=models.CharField(default='2020', help_text='Year of manufacture', max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lostvehicle',
            name='vin_number',
            field=models.CharField(blank=True, help_text='Vehicle Identification Number (VIN) or Chassis Number', max_length=17, null=True),
        ),
        migrations.AddField(
            model_name='lostvehicle',
            name='engine_number',
            field=models.CharField(blank=True, help_text='Engine number if available', max_length=50, null=True),
        ),
    ]
