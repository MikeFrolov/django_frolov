### This file contains all the conditions for homeworks

lesson-4 Django

Создать Пул Реквест

    1. Создать вью функцию которая будет генерировать одного студента с случайными параметрами.
    PATH: /generate-student/ student = Student.objects.create(first_name=faker.first_name) -> id, first_name, last_name, age
    2. Создать вью функцию которая будет генерировать случайных студентов по заданому количеству.
    PATH: /generate-students/?count=100 -> "список" из id, first_name, last_name, age.
    Добавить валидацию count (не быть отрицательным, не больше 100, быть целым числом)
    3. создать модель Group в приложении group добавить несколько полей (название и тип по-желанию)
    4. создать модель Teacher в приложении teachers добавить несколько полей (название и тип по-желанию)
    
    Bonus:
    1. Вывести все группы
    2. Вывести всех учителей

---

Lesson-5 Django queryset, flake8

Результат: линк на пул реквест

    1. установить flake8 и модули (flake8, flake8-import-order, flake8-builtins, flake8-print).
        Почистить код (flake8 ./src)
    
    2. Написать команду которая будет генерировать 100 случайных учителей (python manage.py generate_teachers)
        (https://docs.djangoproject.com/en/2.2/howto/custom-management-commands/)
        добавить параметр который регилирует количество созд. учителей. (по умл. 100)
        (python manage.py generate_teachers 50)
    
    3. Вывести список учителей с возможностью фильтрации по полям age, first_name, last_name.

---

Lesson-6 Forms in Django

    1. Создать форму добавления Student
    
    2. Создать форму добавления Teacher
    
    3. Создать форму добавления Group

    https://django-debug-toolbar.readthedocs.io/en/latest/installation.html

---

Lesson-7 Routing pages. reverse. Editing form in Django

    1. Использовать везде reverse OR {% url %}. В каждом app должен быть свой модуль urls.py
    2. На страничке списка студентов добавить кнопки которые позволят редактировать и удалять студентов.
        После редирект на список.
    3. Полный роутинг для teachers. Список, редактирование, добавление, delete.
    4. Вывести красиво teachers и groups в django admin

Lesson-8 Middleware

    1. Добавить поле phone в модель Student
    2. Сделать raise ошибки если в поле phone ввели не цифры. (StudentCreateForm) django raise error in form
    3. Student, Teacher поля first_name and last_name сделать str.capitalize(). Добавить в сигнал (pre_save).
    4. Создать мидлварь LogMiddleware которая будет записывать параметры request.path, request.method, execution_time (diff),
    если запрос был на админку (/admin/)
    5. Какая разница между поверхностной и глубокой копией (например списков)

    class Logger(models.Model):
    method = models.CharField
    path = ...
    execution_time = ...
    created = DateTimeField (when object was created) auto_now_add???

Lesson-9 Celery and Travis CI

    1. Настроить rabbitmq + celery + celerybeat
        - https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html
        - https://simpleisbetterthancomplex.com/tutorial/2017/08/20/how-to-use-celery-with-django.html
    2. Удалять все логи (модель Logger из предыдущей домашки) "старше" 7 дней, с периодикой раз в день. (created)
    3. Создать форму ContactUS(forms.Form) (title, message, email_from).
       На save формы необходимо отправить письмо на vitalik1996@gmail.com. 
       Письмо должно уходить через celery task. Только пожалуйста, тестируйте на своей почте сначала)
        - https://docs.djangoproject.com/en/3.2/topics/email/
    4. Настроить для своего джанго репозитория Travis CI, и добавить файл конфига в приложении.
        - https://docs.travis-ci.com/user/tutorial/#to-get-started-with-travis-ci-using-github
