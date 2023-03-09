"""
Information Schema
"""

from mongoengine import *

# "your JSON inputs have to have the EXACT SAME field names!"
class Checkpoint(EmbeddedDocument):
    """
    A MongoEngine EmbeddedDocument containing:
    miles: MongoEngine float field, optional, (checkpoint distance in miles)
    km: MongoEngine float field, required, (checkpoint distance in kilometers)
    open: MongoEngine datetime field, required, (checkpoint opening time)
    close: MongoEngine datetime field, required, (checkpoint closing time)
    location: MongoEngine string field, optional, (checkpoint location name)
    """
    miles = FloatField()
    km = FloatField(required=True)
    open = StringField(required=True)       # trying with strings
    close = StringField(required=True)      # trying with strings
    location = StringField()

# "your JSON inputs have to have the EXACT SAME field names!"
class Brevet(Document):
    """
    A MongoEngine document containing:
		start_time: MongoEngine datetime field, required
		brevet_dist: MongoEngine float field, required
		controls: MongoEngine list field of Checkpoints, required
    """
    start_time = StringField(required=True) # trying with strings
    brevet_dist = FloatField(required=True)
    controls = EmbeddedDocumentListField(Checkpoint) # list of Controls
