# Signals allow certain senders to notify a set of receivers that some action has taken place.
# They’re especially useful when many pieces of code may be interested in the same events.
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.dispatch import receiver

@receiver(post_save, sender=User)
def customer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)

#post_save.connect(customer_profile, sender=User)
#for signals to work we need to override the config files ready method in apps.py
