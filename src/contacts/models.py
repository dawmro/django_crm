from django.conf import settings
from django.db import models


User = settings.AUTH_USER_MODEL


# Create your models here.
class Contact(models.Model):
    # default related_name = contact_set
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="mycontacts",  # user.mycontacts.all
    )
    email = models.EmailField()
    notes = models.TextField(blank=True, default="")
    last_edited_by = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name="my_contact_edits",  # user.my_contact_edits.all()
    )

    def get_absolute_url(self):
        return f"/contacts/{self.id}/"
