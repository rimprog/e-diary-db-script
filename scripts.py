import random

from datacenter.models import Schoolkid
from datacenter.models import Mark
from datacenter.models import Chastisement
from datacenter.models import Commendation
from datacenter.models import Lesson


def get_schoolkid(schoolkid_name):
    schoolkids = Schoolkid.objects.all()
    schoolkid = schoolkids.get(full_name__contains=schoolkid_name)

    return schoolkid


def fix_marks(schoolkid_name):
    schoolkid = get_schoolkid(schoolkid_name)
    schoolkid_bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2,3])

    for bad_mark in schoolkid_bad_marks:
        good_mark = random.randint(4, 5)
        bad_mark.points = 5
        bad_mark.save()


def remove_chastisements(schoolkid_name):
    schoolkid = get_schoolkid(schoolkid_name)
    schoolkid_chastisiments = Chastisement.objects.filter(schoolkid=schoolkid)
    schoolkid_chastisiments.delete()


def create_commendation(schoolkid_name, subject_name):
    schoolkid = get_schoolkid(schoolkid_name)
    schoolkid_lessons = Lesson.objects.filter(year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter).filter(subject__title=subject_name)
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
