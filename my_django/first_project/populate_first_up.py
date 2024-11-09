import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

#Fake Pop Script
import random
from first_up.models import topic, Webpage, AccessRecord
from faker import Faker

fakegen = Faker()
topics =["Social", "Search", "Marketplace", "New", "Games"]

def add_topic():
    t = topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):

        #get the topic for the entry
        top = add_topic()

        #create fake  data for the entry
        fake_url = fakegen.url()
        fake_data = fakegen.date()
        fake_name = fakegen.company()

        #create a new Webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        #create a fake access record
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_data)[0]

if __name__ ==  '__main__':
    print("Populating script...")
    populate(20)
    print("Populating complete!")