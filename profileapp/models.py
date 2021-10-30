from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOnefiled(
        User, on_delete=models.CASCADE, related_name='profile')
    # delete = 유저(객체)가 사라질 때, CASCADE = 프로필 같이 삭제, related_name = 바로 접근할 수 있게 이름 지정
    # upload = 서버의 내부저장경로. /media/ 경로 밑에 저장
    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(
        max_length=20, unique=True, null=True)  # unique = 중복방지
    message = models.CharField(max_length=100, null=True)  # 개인메시지(상태메시지)
