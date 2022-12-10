import os , django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','MOC.settings')
django.setup()
from faker import Faker
from django.contrib.auth.models import User

import random


faker = Faker()
for _ in range(20):
    username = faker.first_name()
    last_name = faker.last_name()
    email = username + '@fakemail.com'
    #phone = phn()
    password = username + '@1234'
    user = User.objects.create_user(username=username,password=password)
    user.email = email
    user.first_name = username
    user.last_name = last_name
    user.save()