from django.db import models
from django.utils import timezone
import pyimgur
import datetime
# Create your models here.

CLIENT_ID  = '8590338971a3af7'
SECRET = '9c939ebb5bda20fdb021e549ac503f747ba3f2c1'

class Company(models.Model):
    name = models.CharField('이름', max_length=100)
    logo = models.URLField('로고')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField('카테고리', max_length=255)

    def __str__(self):
        return self.name


class Recruit(models.Model):
    category = models.ForeignKey(Category, related_name='recruits', on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name='recruits', on_delete=models.CASCADE)
    field = models.CharField('모집 분야', max_length=255)
    duedate = models.CharField('마감일', max_length=10)
    place = models.CharField('근무지', max_length=255, default="서울")
    career = models.CharField('경력 구분', max_length=255)
    url = models.URLField('공고주소', null=True, blank=True)
    detail = models.CharField('특이사항', max_length=255, blank=True, null=True)
    comment = models.CharField('코멘트', max_length=255, null=True, blank=True)
    shoot = models.DateField('발송일', blank=True, null=True, default=timezone.now)
    material_text = models.TextField('참고자료', blank=True, null=True)


    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Recruit, self).save()


        if self.material_text:
            ms = self.material_text.split('\n')
            for i in range(int(len(ms) / 2)):
                _text, _link = ms[2*(i-1)], ms[2*(i-1)+1]

                m = Material.objects.create(recruit=self, text=_text, link=_link)

        #
        # for i in range(0, len(sm)):
        #     if not sm[i]:
        #         continue
        #
        #     Material.objects.create(recruit=self, text=sm[i], link=sl[i])
        #     print(sm[i])

        # print(self.img)
        # im = pyimgur.Imgur(CLIENT_ID)
        # image = im.get_image('S1jmapR')
        # print(image.title)

    def __str__(self):
        return '{} / {} / {}'.format(self.company, self.field, self.duedate)


class Material(models.Model):
    recruit = models.ForeignKey(Recruit, related_name='materials', on_delete=models.CASCADE)
    text = models.CharField('텍스트', max_length=255)
    link = models.URLField('링크')
    content = models.CharField('콘텐츠', max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        last_word = self.text.split(' ')[-1]
        _text = self.text.split(' ')[0:-1]


        a = '<a href="{}" target="_blank">{}</a>'.format(self.link, last_word)
        _text.append(a)
        content = ' '.join(_text)
        self.content=content
        super(Material, self).save()

    def __str__(self):
        return '{}: {}'.format(self.recruit.company, self.text)