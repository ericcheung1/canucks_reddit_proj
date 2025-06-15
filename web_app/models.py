from mongoengine import Document, StringField, IntField, ListField, FloatField, EmbeddedDocument, EmbeddedDocumentField, URLField

class Reply(EmbeddedDocument):
    comment_id = StringField(required=True)
    author = StringField(default="[deleted]")
    body = StringField(default="[deleted]")
    compound_sentiment = FloatField()
    neg_sentiment = FloatField()
    neu_sentiment = FloatField()
    pos_sentiment = FloatField()
    utc_created = IntField()

    replies = ListField(EmbeddedDocumentField("Reply"))

class Comment(EmbeddedDocument):
    comment_id = StringField(required=True)
    author = StringField(default="[deleted]")
    body = StringField(default="[deleted]")
    compound_sentiment = FloatField()
    neg_sentiment = FloatField()
    neu_sentiment = FloatField()
    pos_sentiment = FloatField()
    utc_created = IntField()

    replies = ListField(EmbeddedDocumentField(Reply))

class Post(Document):
    post_id = StringField(required=True, unique=True)
    title = StringField(required=True)
    author = StringField(default="[deleted]")
    score = IntField(default=0)
    avg_neg = FloatField()
    avg_neu = FloatField()
    avg_pos = FloatField()
    avg_compound = FloatField()
    neg_count = IntField()
    neu_count = IntField()
    pos_count = IntField()
    total_bodies = IntField()
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