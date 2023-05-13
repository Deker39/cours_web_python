from django.db.models import *


class UserNews(Model):
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    email = CharField(max_length=100)
    password = CharField(max_length=100)
    ban = BooleanField()
    ban_time = DateTimeField()


class NewsPost(Model):
    title = CharField(max_length=100)
    content = CharField(max_length=100)


class CommentPost(Model):
    auth = ForeignKey(UserNews, on_delete=CASCADE, related_name='auth')
    post = ForeignKey(NewsPost, on_delete=CASCADE, related_name='post')
    content = CharField(max_length=100)
    date = DateTimeField(auto_now=True)


class ImageNewsPost(Model):
    newspost = ForeignKey(NewsPost, on_delete=CASCADE, related_name='image')
    image = ImageField(upload_to='news/')


class ParamsProject(Model):
    background_color = CharField(max_length=100)
    color_text = CharField(max_length=100)
    size_text = CharField(max_length=100)


class PostCommentCount(Model):
    id = IntegerField(primary_key=True)
    news = ForeignKey('NewsPost', on_delete=CASCADE, related_name='news_comment_counts')
    comment_count = IntegerField()

    class Meta:
        managed = False
        db_table = 'news_comment_count'

