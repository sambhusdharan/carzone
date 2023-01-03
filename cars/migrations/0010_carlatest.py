# Generated by Django 3.2.12 on 2022-12-15 08:45

import ckeditor.fields
import datetime
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_alter_car_no_of_owners'),
    ]

    operations = [
        migrations.CreateModel(
            name='carlatest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartitle', models.CharField(max_length=225)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District Of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'India'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], verbose_name='year')),
                ('condition', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', ckeditor.fields.RichTextField()),
                ('car_photo_1', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('car_photo_2', models.ImageField(blank=True, upload_to='pages/%Y/%m/%d/')),
                ('car_photo_3', models.ImageField(blank=True, upload_to='pages/%Y/%m/%d/')),
                ('car_photo_4', models.ImageField(blank=True, upload_to='pages/%Y/%m/%d/')),
                ('car_photo_5', models.ImageField(blank=True, upload_to='pages/%Y/%m/%d/')),
                ('feature', multiselectfield.db.fields.MultiSelectField(choices=[('Cruise Control', 'Cruise Control'), ('Audio Interface', 'Audio Interface'), ('Airbags', 'Airbags'), ('Air Conditioning', 'Air Conditioning'), ('Seat Heating', 'Seat Heating'), ('Alarm System', 'Alarm System'), ('ParkAssist', 'ParkAssist'), ('Power Steering', 'Power Steering'), ('Reversing Camera', 'Reversing Camera'), ('Direct Fuel Injection', 'Direct Fuel Injection'), ('Auto Start/Stop', 'Auto Start/Stop'), ('Wind Deflector', 'Wind Deflector'), ('Bluetooth Handset', 'Bluetooth Handset')], max_length=225)),
                ('body_style', models.CharField(max_length=225)),
                ('engine', models.CharField(max_length=225)),
                ('transmission', models.CharField(max_length=225)),
                ('interior', models.CharField(max_length=225)),
                ('miles', models.IntegerField()),
                ('doors', models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=100)),
                ('seats', models.CharField(choices=[('2', '2'), ('4', '4'), ('5', '5'), ('7', '7'), ('9', '9'), ('12', '12')], max_length=100)),
                ('vehicle_no', models.CharField(max_length=225)),
                ('milage', models.IntegerField()),
                ('fuel_type', models.CharField(choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Hybrid', 'Hybrid'), ('Electric', 'Electric'), ('Hydrogen', 'Hydrogen')], max_length=225)),
                ('no_of_owners', models.CharField(choices=[('First owner', 'First owner'), ('Second owner', 'Second owner'), ('Third owner', 'Third owner'), ('Fourth owner', 'Fourth owner'), ('Fifth owner', 'Fifth owner')], max_length=100)),
                ('sale', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
