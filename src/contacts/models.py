from django.contrib.contenttypes.fields import GenericRelation
from django.conf import settings
from django.db import models
from events.models import Event


User = settings.AUTH_USER_MODEL


# Create your models here.
class Contact(models.Model):
    # default related_name = contact_set
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="mycontacts",  # user.mycontacts.all
    )
    email = models.EmailField(db_index=True)
    first_name = models.CharField(max_length=120, default="", blank=True)
    lastfirst_name = models.CharField(max_length=120, default="", blank=True)
    notes = models.TextField(blank=True, default="")
    last_edited_by = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name="my_contact_edits",  # user.my_contact_edits.all()
    )
    last_sync = models.DateTimeField(
        auto_now_add=False, auto_now=False, blank=True, null=True
    )
    events = GenericRelation(Event)  # contact_instance.events.all()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return f"/contacts/{self.id}/"
