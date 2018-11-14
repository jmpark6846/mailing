from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class Recruit(models.Model):
    company = models.CharField('회사명', max_length=255)
    field = models.CharField('모집 분야', max_length=255)
    duedate = models.DateField('마감일', blank=True, null=True)
    place = models.CharField('근무지', max_length=255)
    career = models.CharField('경력 구분', max_length=255)
    detail = models.CharField('특이사항', max_length=255)
    shoot = models.DateField('발송일', blank=True, null=True, default=timezone.now)

    def due(self):
        if not self.duedate:
            return 'ASAP'
        return datetime.datetime.strptime(self.duedate, '~m/d')

    def __str__(self):
        return '{} / {} / {}'.format(self.company, self.field, self.duedate)

