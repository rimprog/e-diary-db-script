import random

from django.shortcuts import get_object_or_404
from django.core.exceptions import MultipleObjectsReturned
from django.http import Http404

from datacenter.models import Schoolkid
from datacenter.models import Mark
from datacenter.models import Chastisement
from datacenter.models import Commendation
from datacenter.models import Lesson
from datacenter.models import Subject


def get_schoolkid(schoolkid_name):
    try:
        schoolkid = get_object_or_404(
            Schoolkid,
            full_name__contains=schoolkid_name
        )

        return schoolkid

    except Http404:
        print('ERROR! Schoolkid with name "{}" not found. Try refine your search query'.format(schoolkid_name))

    except MultipleObjectsReturned:
        print('ERROR! Finded more than one Schoolkid with name "{}". Try refine your search query'.format(schoolkid_name))


def get_subject(subject_title, year_of_study):
    try:
        subject = get_object_or_404(
            Subject,
            title=subject_title,
            year_of_study=year_of_study
        )

        return subject

    except Http404:
        print('ERROR! Subject with title "{}" and "{}" years of study not found. Try refine your search query'.format(subject_title, year_of_study))

    except MultipleObjectsReturned:
        print('ERROR! Finded more than one Subject with title "{}" and "{}" years of study. Try refine your search query'.format(subject_title, year_of_study))


def fix_marks(schoolkid_name):
    schoolkid = get_schoolkid(schoolkid_name)
    schoolkid_bad_marks = Mark.objects.filter(
        schoolkid=schoolkid,
        points__in=[2,3]
    )

    for bad_mark in schoolkid_bad_marks:
        good_mark = random.randint(4, 5)
        bad_mark.points = 5
        bad_mark.save()


def remove_chastisements(schoolkid_name):
    schoolkid = get_schoolkid(schoolkid_name)
    schoolkid_chastisiments = Chastisement.objects.filter(schoolkid=schoolkid)
    schoolkid_chastisiments.delete()


def create_commendation(schoolkid_name, subject_title):
    schoolkid = get_schoolkid(schoolkid_name)
    subject = get_subject(subject_title, schoolkid.year_of_study)
    schoolkid_lessons = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject=subject
    )
    last_schoolkid_lesson = schoolkid_lessons.order_by('-date')[0]

    commendations = [
        'Молодец!',
        'Отлично!',
        'Хорошо!',
        'Гораздо лучше, чем я ожидал!',
        'Ты меня приятно удивил!',
        'Великолепно!',
        'Прекрасно!',
        'Ты меня очень обрадовал!',
        'Именно этого я давно ждал от тебя!',
        'Сказано здорово – просто и ясно!',
        'Ты, как всегда, точен!',
        'Очень хороший ответ!',
        'Талантливо!',
        'Ты сегодня прыгнул выше головы!',
        'Я поражен!',
        'Уже существенно лучше!',
        'Потрясающе!',
        'Замечательно!',
        'Прекрасное начало!',
        'Так держать!',
        'Ты на верном пути!',
        'Здорово!',
        'Это как раз то, что нужно!',
        'Я тобой горжусь!',
        'С каждым разом у тебя получается всё лучше!',
        'Мы с тобой не зря поработали!',
        'Я вижу, как ты стараешься!',
        'Ты растешь над собой!',
        'Ты многое сделал, я это вижу!',
        'Теперь у тебя точно все получится!'
    ]

    commendation = Commendation.objects.create(
        text=random.choice(commendations),
        created=last_schoolkid_lesson.date,
        schoolkid=schoolkid,
        subject=last_schoolkid_lesson.subject,
        teacher=last_schoolkid_lesson.teacher
    )
