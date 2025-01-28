from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models


# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Contributor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture_url = models.URLField()

    def __str__(self):
        return self.user.username


class CandidateRestaurant(models.Model):
    display_name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.PointField(geography=True, srid=4326)
    # 画像は任意でpolls/static/media/に保存される
    photos = models.ImageField(blank=True, null=True, upload_to='polls/static/media/')
    # 初めての投稿者のレビューは任意
    review = models.TextField(blank=True, null=True)
    # TODO: お店のレビューはRestaurantReviewモデルで管理する
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.display_name

class PassedRestaurant(models.Model):
    CUISINE_TYPE = (
        ('ramen_restaurant', 'ラーメン屋'),
        ('fast_food_restaurant', 'ファーストフード'),
        ('chinese_restaurant', '中華料理'),
        ('french_restaurant', 'フランス料理'),
        ('japanese_restaurant', '日本料理'),
        ('italian_restaurant', 'イタリア料理'),
        ('sushi_restaurant', '寿司屋'),
        ('steak_house', 'ステーキハウス'),
        ('bakery', 'パン屋'),
        ('cafe', 'カフェ'),
        ('bar', 'バー'),
        ('meal_takeaway', 'テイクアウト')
    )
    candidate_restaurant = models.OneToOneField(CandidateRestaurant, on_delete=models.CASCADE)
    primary_type_display_name = models.CharField(max_length=255, choices=CUISINE_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
