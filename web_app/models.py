from mongoengine import Document, StringField, IntField, ListField, EmbeddedDocument, EmbeddedDocumentField, URLField

class Reply(EmbeddedDocument):
    comment_id = StringField(required=True)
    author = StringField(default="[deleted]")
    body = StringField(default="[deleted]")
    utc_created = IntField()

    replies = ListField(EmbeddedDocumentField("Reply"))

class Comment(EmbeddedDocument):
    comment_id = StringField(required=True)
    author = StringField(default="[deleted]")
    body = StringField(default="[deleted]")
    utc_created = IntField()

    replies = ListField(EmbeddedDocumentField(Reply))

class Post(Document):
    post_id = StringField(required=True, unique=True)
    title = StringField(required=True)
    author = StringField(default="[deleted]")
    score = IntField(default=0)
    url = URLField()
    utc_created = IntField()

    comments = ListField(EmbeddedDocumentField(Comment))

    meta = {
        "collection": "post_game_threads",
        "indexes": [
            {"fields": ["post_id"], "unique": True},
            {"fields": ["title"]},
            {"fields": ["author"]},
            {"fields": ["-utc_created"]}
        ]
    }