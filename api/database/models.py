"""
Information Schema
"""


from mongoengine import *


# not going to directly store checkpoints as rows (documents) anywhere,
# going to put checkpoint into a brevet, and then store brevetS

class Checkpoint(EmbeddedDocument):
    """
    A MongoEngine EmbeddedDocument containing:
    distance: MongoEngine float field, required, (checkpoint distance in kilometers),
    location: MongoEngine string field, optional, (checkpoint location name),
    open_time: MongoEngine datetime field, required, (checkpoint opening time),
    close_time: MongoEngine datetime field, required, (checkpoint closing time).
    """

    # FIXME: check MongoEngine docs and slides
    # distance = FloatField(required=True)
    # location = StringField(required=False)
    # open_time = EmbeddedDocumentDatetimeField(required=True)    # "dont have to do datetimes, but strongly recommended"
    # close_time = EmbeddedDocumentDatetimeField(required=True)   # "dont have to do datetimes, but strongly recommended"
    pass


class Brevet(Document):
    """
    A MongoEngine document containing:
		length: MongoEngine float field, required
		start_time: MongoEngine datetime field, required
		checkpoints: MongoEngine list field of Checkpoints, required
    """

    # FIXME: 
    # the non-StringFields will probably be of the form EmbeddedDocument____Field(...)
    # check MongoEngine docs and slides
    
    length = FloatField(required=True)
    start_time = EmbeddedDocumentDatetimeField(required=True)

    # use consistent key names
    # "must be EXACTLY the same thing as what you're gonna pass in when you're inserting this"
    checkpoints = EmbeddedDocumentListField(Checkpoint) # list of Checkpoints
    pass
