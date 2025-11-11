from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.db import models
from timescale.db.models.models import TimescaleModel

# from contacts.models import Contact


User = settings.AUTH_USER_MODEL


class Event(TimescaleModel):
    class EventType(models.TextChoices):
        # enum = "db_val", "Display value"
        UNKNOWN = "unknown", "Unknown Event"
        CREATED = "created", "Create Event"
        SYNC = "sync", "Sync Event"
        VIEWED = "viewed", "View Event"
        SAVED = "saved", "Save or Update Event"

    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        help_text="Performed by user",
        related_name="myevents",  # user.myevents.all
    )
    type = models.CharField(
        max_length=40, default=EventType.VIEWED, choices=EventType.choices
    )
    object_id = models.PositiveBigIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey("content_type", "object_id")
    # timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [models.Index(fields=["content_type", "object_id"])]
