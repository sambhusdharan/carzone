from datetime import datetime
from ckeditor.fields import RichTextField
from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class car(models.Model):
    state_choice=(
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'India'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
          )
    year_choice=[]
    for r in range(2000,(datetime.now().year+1)):
       year_choice.append((r, r))

    features_choices = (
        ('Cruise Control', 'Cruise Control'),# first value for storing to database and other value for displaying to the user in the admin pannel
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
                      )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    seat_choice=(
        ('2','2'),
        ('4','4'),
        ('5','5'),
        ('7','7'),
        ('9','9'),
        ('12','12'),
    )
    owners_list=(
        ('First owner','First owner'),
        ('Second owner','Second owner'),
        ('Third owner','Third owner'),
        ('Fourth owner','Fourth owner'),
        ('Fifth owner','Fifth owner'),
    )

    fuel_type=(
        ('Petrol','Petrol'),
        ('Diesel','Diesel'),
        ('Hybrid','Hybrid'),
        ('Electric','Electric'),
        ('Hydrogen','Hydrogen'),
    )

    cartitle=models.CharField(max_length=225)
    city = models.CharField(max_length=100)
    state = models.CharField(choices=state_choice,max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('year'),choices=year_choice)
    condition = models.CharField(max_length=100)
    price = models.IntegerField()
#    Discount_price=models.IntegerField()
    description = RichTextField()
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/',)
    car_photo_2 = models.ImageField(upload_to='pages/%Y/%m/%d/',blank=True)
    car_photo_3 = models.ImageField(upload_to='pages/%Y/%m/%d/',blank=True)
    car_photo_4 = models.ImageField(upload_to='pages/%Y/%m/%d/',blank=True)
    car_photo_5 = models.ImageField(upload_to='pages/%Y/%m/%d/',blank=True)
    feature = MultiSelectField(choices=features_choices,max_length=225)
    body_style = models.CharField(max_length=225)
    engine = models.CharField(max_length=225)
    transmission = models.CharField(max_length=225)
    interior = models.CharField(max_length=225)
    miles = models.IntegerField()
    doors = models.CharField(choices=door_choices,max_length=100)
    seats = models.CharField(choices=seat_choice,max_length=100)
    vehicle_no = models.CharField(max_length=225)
    milage = models.IntegerField()
    fuel_type = models.CharField(choices=fuel_type,max_length=225)
    no_of_owners = models.CharField(choices=owners_list,max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.cartitle

class carlatest(models.Model):
        state_choice = (
            ('AL', 'Alabama'),
            ('AK', 'Alaska'),
            ('AZ', 'Arizona'),
            ('AR', 'Arkansas'),
            ('CA', 'California'),
            ('CO', 'Colorado'),
            ('CT', 'Connecticut'),
            ('DE', 'Delaware'),
            ('DC', 'District Of Columbia'),
            ('FL', 'Florida'),
            ('GA', 'Georgia'),
            ('HI', 'Hawaii'),
            ('ID', 'Idaho'),
            ('IL', 'Illinois'),
            ('IN', 'India'),
            ('IA', 'Iowa'),
            ('KS', 'Kansas'),
            ('KY', 'Kentucky'),
            ('LA', 'Louisiana'),
            ('ME', 'Maine'),
            ('MD', 'Maryland'),
            ('MA', 'Massachusetts'),
            ('MI', 'Michigan'),
            ('MN', 'Minnesota'),
            ('MS', 'Mississippi'),
            ('MO', 'Missouri'),
            ('MT', 'Montana'),
            ('NE', 'Nebraska'),
            ('NV', 'Nevada'),
            ('NH', 'New Hampshire'),
            ('NJ', 'New Jersey'),
            ('NM', 'New Mexico'),
            ('NY', 'New York'),
            ('NC', 'North Carolina'),
            ('ND', 'North Dakota'),
            ('OH', 'Ohio'),
            ('OK', 'Oklahoma'),
            ('OR', 'Oregon'),
            ('PA', 'Pennsylvania'),
            ('RI', 'Rhode Island'),
            ('SC', 'South Carolina'),
            ('SD', 'South Dakota'),
            ('TN', 'Tennessee'),
            ('TX', 'Texas'),
            ('UT', 'Utah'),
            ('VT', 'Vermont'),
            ('VA', 'Virginia'),
            ('WA', 'Washington'),
            ('WV', 'West Virginia'),
            ('WI', 'Wisconsin'),
            ('WY', 'Wyoming'),
        )
        year_choice = []
        for r in range(2000, (datetime.now().year + 1)):
            year_choice.append((r, r))

        features_choices = (
            ('Cruise Control', 'Cruise Control'),
            # first value for storing to database and other value for displaying to the user in the admin pannel
            ('Audio Interface', 'Audio Interface'),
            ('Airbags', 'Airbags'),
            ('Air Conditioning', 'Air Conditioning'),
            ('Seat Heating', 'Seat Heating'),
            ('Alarm System', 'Alarm System'),
            ('ParkAssist', 'ParkAssist'),
            ('Power Steering', 'Power Steering'),
            ('Reversing Camera', 'Reversing Camera'),
            ('Direct Fuel Injection', 'Direct Fuel Injection'),
            ('Auto Start/Stop', 'Auto Start/Stop'),
            ('Wind Deflector', 'Wind Deflector'),
            ('Bluetooth Handset', 'Bluetooth Handset'),
        )

        door_choices = (
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
        )

        seat_choice = (
            ('2', '2'),
            ('4', '4'),
            ('5', '5'),
            ('7', '7'),
            ('9', '9'),
            ('12', '12'),
        )
        owners_list = (
            ('First owner', 'First owner'),
            ('Second owner', 'Second owner'),
            ('Third owner', 'Third owner'),
            ('Fourth owner', 'Fourth owner'),
            ('Fifth owner', 'Fifth owner'),
        )

        fuel_type = (
            ('Petrol', 'Petrol'),
            ('Diesel', 'Diesel'),
            ('Hybrid', 'Hybrid'),
            ('Electric', 'Electric'),
            ('Hydrogen', 'Hydrogen'),
        )

        cartitle = models.CharField(max_length=225)
        city = models.CharField(max_length=100)
        state = models.CharField(choices=state_choice, max_length=100)
        color = models.CharField(max_length=100)
        model = models.CharField(max_length=100)
        year = models.IntegerField(('year'), choices=year_choice)
        condition = models.CharField(max_length=100)
        price = models.IntegerField()
        #    Discount_price=models.IntegerField()
        description = RichTextField()
        car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', )
        car_photo_2 = models.ImageField(upload_to='pages/%Y/%m/%d/', blank=True)
        car_photo_3 = models.ImageField(upload_to='pages/%Y/%m/%d/', blank=True)
        car_photo_4 = models.ImageField(upload_to='pages/%Y/%m/%d/', blank=True)
        car_photo_5 = models.ImageField(upload_to='pages/%Y/%m/%d/', blank=True)
        feature = MultiSelectField(choices=features_choices, max_length=225)
        body_style = models.CharField(max_length=225)
        engine = models.CharField(max_length=225)
        transmission = models.CharField(max_length=225)
        interior = models.CharField(max_length=225)
        miles = models.IntegerField()
        doors = models.CharField(choices=door_choices, max_length=100)
        seats = models.CharField(choices=seat_choice, max_length=100)
        vehicle_no = models.CharField(max_length=225)
        milage = models.IntegerField()
        fuel_type = models.CharField(choices=fuel_type, max_length=225)
        no_of_owners = models.CharField(choices=owners_list, max_length=100)
        sale = models.BooleanField(default=False)
        created_date = models.DateTimeField(default=datetime.now)

        def __str__(self):
            return self.cartitle