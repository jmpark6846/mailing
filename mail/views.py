from django.shortcuts import render, HttpResponse, redirect
from .models import Recruit, Category, Material, Company
from .imgur import load_images_from_imgur
import pyimgur
import openpyxl


def mail_detail(request):
    recruits = Recruit.objects.all()
    categories = Category.objects.all()
    context = { 'recruits' : recruits, 'categories': categories }
    company = Company.objects.filter(logo='')
    print(company)
    return render(request, 'mail/mail_detail.html', context)


def load_images(request):
    img_dict = load_images_from_imgur()
    recruits = Recruit.objects.all()

    for r in recruits:

        if r.company.name in img_dict:
            c = Company.objects.get(name=r.company.name)
            link = img_dict[r.company.name]

            c.logo = link
            c.save()

    return HttpResponse('success')


def load_file(request):
    wb = openpyxl.load_workbook('/home/joonmo/data.xlsx')

    ws = wb['채용공고 세부내용']

    for i, r in enumerate(ws.rows):
        if i==0:
            continue

        category, created = Category.objects.get_or_create(name=r[4].value)
        company, created = Company.objects.get_or_create(name=r[5].value)

        recruit_data = {
            'category': category,
            'company': company,
            'field': r[6].value,
            'duedate': r[8].value,
            'place':r[9].value,
            'career':r[10].value,
            'url':r[11].value,
            'detail': r[12].value,
            'comment': r[15].value,
            'shoot':r[3].value,
            'material_text': r[13].value
        }


        r = Recruit.objects.create(**recruit_data)
        # print(r)


    return redirect('/')


# jobaid@naver.com, choikyukang@gmail.com
#