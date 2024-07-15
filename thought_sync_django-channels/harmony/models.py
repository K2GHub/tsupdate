from uuid import uuid4
from django.db import models
from django.conf import settings

from .validators import image_size_validator

# Create your models here.
"""
    ABSTRACT MODEL = WithCreateUpdateTrashTime

    USES:
        - Any models that need created_at, updated_at, and/or trashed_at fields can inherit from it
        - Avoid errors in repetition

    INHERITING MODELS : 
        - UserProfile
        - Synch
        - SynchMembership
        - Stream
        - Note
        - TextNote
        - ImageNote
"""
class WithCreateUpdateTrashTime(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    trashed_at = models.DateTimeField(null=True)
    class Meta:
        abstract = True

# end of WithCreateUpdateTrashTime


"""
    MODEL = UserProfile
    USES:
        - more info about the user that is outside of the necessary for user database management
    NOTICES:
        -
    TO DO:
        - 
    RELATED FIELDS :
        - mysynchs : model = Synch : synchs created by this user
        - synchs : model = SynchMembership : list of synchs this profile owner is part of
        - mystreams : model = Stream : streams created by this user
        - streams : model = StreamMembership : list of streams this profile owner is part of
        - notes : model = Note : notes created by this user
"""
class UserProfile (WithCreateUpdateTrashTime):
    id = models.UUIDField(primary_key=True, default=uuid4)
    # delete user when user profile is deleted
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, related_name="profile", unique=True)
    birthday = models.DateField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    picture = models.ImageField(upload_to="users/pictures", null=True, blank=True, validators=[image_size_validator])
    
# end of UserProfile


"""
maybe create a customer discovery model here to track the data about 
the customer's interest in using the app or some other potentially importand data about what we can help them with 
"""


"""
    MODEL = Synch
    USES:
        - info about a synch or major chat or group chat
    NOTICES:
        - 
    TO DO:
        - 
    RELATED FIELDS :
        - streams : model = Stream : streams assossiated with this synch
        - members : model = SynchMembership : profiles of each member in the synch
"""
class Synch (WithCreateUpdateTrashTime):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.TextField(null=True, blank=True)
    # the reason why we do not automatically delete the synch if a user delete their account or profile is
    # because there might be others that are still using it
    creator = models.ForeignKey(UserProfile, null=True, on_delete=models.SET_NULL, related_name="mysynchs")
    picture = models.ImageField(upload_to="synchs/pictures", null=True, blank=True, validators=[image_size_validator])
    
# end of Synch


"""
    MODEL = SynchMembership
    USES:
        - to track what user profiles are in what synchs
    NOTICES:
        - 
    TO DO:
        - 
    RELATED FIELDS :
        - 
"""
class SynchMembership (WithCreateUpdateTrashTime):
    id = models.UUIDField(primary_key=True, default=uuid4)
    synch = models.ForeignKey(Synch, on_delete=models.CASCADE, related_name="members")
    member = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="synchs")
    
    class Meta:
        # ensure that a pair is unique to avoid duplicates
        unique_together = ('synch', 'member')

# end of SynchMembership

"""
    MODEL = Stream
    USES:
        - info about a stream or topic inside a synch
    NOTICES:
        - 
    TO DO:
        - 
    RELATED FIELDS :
        - notes : model = Note : notes (collection of notes) inside this stream (line of notes)
        - members : model = StreamMembership : profiles of each member in the stream
"""
class Stream (WithCreateUpdateTrashTime):
    EVERYONE = 'EVE'
    ME_ONLY = 'MEO'
    CUSTOM = 'CUS'

    MEMBERSHIP_TYPE_CHOICES = [
        (EVERYONE, 'Everyone'),
        (ME_ONLY, 'Me Only'),
        (CUSTOM, 'Custom'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid4)
    # if a whole synch is deleted, everything in it should be deleted
    synch = models.ForeignKey(Synch, on_delete=models.CASCADE, related_name="streams")
    name = models.TextField(null=True, blank=True)
    creator = models.ForeignKey(UserProfile, null=True, on_delete=models.SET_NULL, related_name="mystreams")
    membership_type = models.CharField(max_length=3, choices=MEMBERSHIP_TYPE_CHOICES, default=EVERYONE)

# end of Stream


"""
    MODEL = StreamMembership
    USES:
        - to track membership of the user to a stream
        _ to track customization (order, mark_resolved, etc) of user to stream
    NOTICES:
        - 
    TO DO:
        - 
    RELATED FIELDS :
        -  : model =  : 
"""
class StreamMembership (WithCreateUpdateTrashTime):
    NEW = 'NEW'
    ACTIVE = 'ACT'
    RESOLVED = 'RES'
    DOES_NOT_CONCERN_ME = 'DNC'

    STATUS_CHOICES = [
        (NEW, 'New'),
        (ACTIVE, 'Active'),
        (RESOLVED, 'Resolved'),
        (DOES_NOT_CONCERN_ME, 'Does Not Concern Me'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid4)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE, related_name="members")
    member = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="streams")
    order = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default=NEW)

    class Meta:
        # ensure that a pair is unique to avoid duplicates
        unique_together = ('stream', 'member')

# end of StreamMembership


"""
    MODEL = Note
    USES:
        - to hold a bulk of notes (text, image, video, files)
        - to know what photos, video, or files are created in a bulk
            + this helps us put them in a bulk container in the frontend
    NOTICES:
        - 
    TO DO:
        - 
    RELATED FIELDS :
        - text : model = TextNote : text content of this note
        - images : model = ImageNote : collection of images content of this note
"""
class Note (WithCreateUpdateTrashTime):
    id = models.UUIDField(primary_key=True, default=uuid4)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE, related_name="notes")
    taker = models.ForeignKey(UserProfile, null=True, on_delete=models.SET_NULL, related_name="notes")

# end of Note


"""
    MODEL = TextNote
    USES:
        - 
    NOTICES:
        - 
    TO DO:
        - 
    RELATED FIELDS :
        -  : model =  : 
"""
class TextNote (WithCreateUpdateTrashTime):
    id = models.UUIDField(primary_key=True, default=uuid4)
    text = models.TextField()
    note = models.OneToOneField(Note, on_delete=models.CASCADE, related_name="text")

# end of TextNote


"""
    MODEL = ImageNote
    USES:
        - 
    NOTICES:
        - 
    TO DO:
        - 
    RELATED FIELDS :
        -  : model =  : 
"""
class ImageNote (WithCreateUpdateTrashTime):
    id = models.UUIDField(primary_key=True, default=uuid4)
    image = models.ImageField(upload_to="notes/images", validators=[image_size_validator])
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name="images")

# end of ImageNote



