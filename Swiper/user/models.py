from django.db import models

class User(models.Model):
    '''
       phonenum ⼿机号
       nickname 昵称
       sex 性别
       birth_year 出⽣年
       birth_month 出⽣⽉
       birth_day 出⽣⽇
       avatar 个⼈形象
       location 常居地
    '''
    SEX = (
        ('0',"未知"),
        ('1',"男"),
        ('2',"女")
    )
    LOCATIONS = (
        ('gz','广州'),
        ('bj','北京'),
        ('sh','上海'),
        ('sz','深圳'),
        ('wh','武汉'),
        ('hz','杭州'),
        ('cq','重庆'),
        ('cd','成都'),
        ('tj','天津'),
    )
    phonenum = models.CharField(max_length=11,unique=True)
    nickname = models.CharField(max_length=16)
    sex = models.CharField(max_length=1,choices=SEX,default='0')
    birthday_year = models.IntegerField(default=2000)
    birthday_month = models.IntegerField(default=1)
    birthday_day = models.IntegerField(default=1)
    avatar = models.CharField(max_length=256)
    location = models.CharField(max_length=16,choices=LOCATIONS,default="gz")

    class Meta():
        db_table = "users"