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
        - Stream
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
        - mystreams : model = Stream : streams created by this user
        - notes : model = Note : notes created by this user
"""
class UserProfile (WithCreateUpdateTrashTime):
    id = models.UUIDField(primary_key=True, default=uuid4)
    # delete user when user profile is deleted
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, related_name="profile", unique=True)
    birthday = models.DateField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    picture = models.ImageField(upload_to="users/pictures", validators=[image_size_validator])
    

# end of UserProfile



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
"""
class Synch (WithCreateUpdateTrashTime):
    id = models.UUIDField(primary_key=True, default=uuid4)
    title = models.TextField(null=True, blank=True)
    # the reason why we do not automatically delete the synch if a user delete their account or profile is
    # because there might be others that are still using it
    created_by = models.ForeignKey(UserProfile, null=True, on_delete=models.SET_NULL, related_name="mysynchs")
    picture = models.ImageField(upload_to="synchs/pictures", validators=[image_size_validator])
    

# end of Synch


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
"""
class Stream (WithCreateUpdateTrashTime):
    id = models.UUIDField(primary_key=True, default=uuid4)
    # if a whole synch is deleted, everything in it should be deleted
    synch = models.ForeignKey(Synch, on_delete=models.CASCADE, related_name="streams")
    title = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(UserProfile, null=True, on_delete=models.SET_NULL, related_name="mystreams")
    
# end of Stream


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
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE, related_name="notes")
    sender = models.ForeignKey(UserProfile, null=True, on_delete=models.SET_NULL, related_name="notes")

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
    image = models.ImageField(upload_to="notes/images", validators=[image_size_validator])
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name="images")

# end of ImageNote



