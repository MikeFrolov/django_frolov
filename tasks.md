### This file contains all the conditions for homeworks

---
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

---
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

---
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

---
Lesson-10 Links and Parsers

    1. Добавить в модель Group внешние ключи на куратора (Teacher) и студентов (Student).
    2. Вывести соответствующую информацию в таблицах и в админке (html). (/group/list/)
    3. Обновить скрипт по генерации случайных учителей, чтоб к каждому новому учителю генерировалась 1
        группа со случайным количеством студентов (до 10) python manage.py generate_teachers
    4. Добавить парсер курс валют, который будет раз в день брать текущий курс USD и EUR из
        monobank и нацбанка.в базу.

---
Lesson-11 Templates

    1. подключить https://getbootstrap.com/docs/4.5/getting-started/introduction/
    2. Показать список курсов валют в таблице https://getbootstrap.com/docs/4.5/content/tables/
    3. Добавить проверки в Travis CI
        - python manage.py validate_templates
        - python manage.py check
        - python manage.py makemigrations --check --dry-run
        - pip check

---
Lesson-12 Run online tests

    1. Пройти все 7 тестов, сделать работу над ошибками:
        https://www.tutorialsteacher.com/online-test/python-test

    Не нужно перепроходить все тесты по несколько раз ради лучшей оценки, мне важно чтоб вы поняли где у вас есть
        пробелы. Скинуть скрины результатов.

---
Lesson-13 Class-based views

    1. Кастомные страницы для статусов ответа: 500, 404:
        https://docs.djangoproject.com/en/2.2/topics/http/views/#customizing-error-views
        https://docs.djangoproject.com/en/2.2/ref/views/#error-views
    2. Перевести все вью функций во View классы:
        Списки:
            https://docs.djangoproject.com/en/3.2/ref/class-based-views/generic-display/#listview
        Формы:
            https://docs.djangoproject.com/en/3.2/ref/class-based-views/generic-editing/
        Кастомные вью:
            https://docs.djangoproject.com/en/3.2/ref/class-based-views/base/

---
Lesson-14 Cover the project with tests

    1. Покрыть интеграционными тестами все апки. Например:
        get /students/ -> assert students.count == 0
        get /generate-students/100 -> assert students.count == 100
        post /edit-student/1 -> assert students.count == 1 AND student.data ==
        post /create-student/ -> assert students.count == 1
        тест для правильного/неправильного телефона студента
        тесты для мидлварей
        и т.д.

        И так далее для преподов, групп, и курсов валют.
        Чтоб понять, какие еще файлы и строки не покрыты тестами, рекомендую использовать:
        https://pytest-cov.readthedocs.io/en/latest/readme.html

    2. добавить команду pytest -s в travis

---
Lesson-15 Heroku deploy

    Задеплоить ваше приложенько на heroku:
        https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/Deployment

    Если у вас Windows - вместо gunicorn используйте waitress (соответсвенно в Procfile будет другая команда
        старта приложения):
        https://docs.pylonsproject.org/projects/waitress/en/latest/runner.html#invocation

    Не забудьте выставить DJANGO_SECRET_KEY!

---
Lesson-16 Registration

    1. Добавить странички регистрации и логина
    2. Применить джанго флоу по востановлению пароля 
        (пример: https://www.ordinarycoders.com/blog/article/django-password-reset)
    3. Создать страницу для смены пароля. 
        Форма должна иметь 3 поля (current password, new password, confirm new password)
    4. Ограничить создание, модификацию и удаление всех сущностей только зарегистрированным пользователям.

---
Lesson-17 Find the number of O(?) Operations for each function

    1. 
    num = 10
    def deductOne(num):
        num -= 1
        return num

    print(deductOne(num)

    2.
    testList = [1, 43, 31, 21, 6, 96, 48, 13, 25, 5]
    def someSort(testList):
        for i in range(len(testList)):
            for j in range(i + 1, len(testList)):
                if testList[j] < testList[i]:
                    testList[j], testList[i] = testList[i], testList[j]
                    print(testList)

    print(someSort(testList))

    3.
    num = 10
    def divide(num):
        while num > 1:
            num /= 2
            print(num)
        return num

    print(divide(num))

    4.
    testList = [1, 43, 31, 21, 6, 96, 48, 13, 25, 5]
    def wonderSort(testList):
        if len(testList) < 2:
            return testList
        middle = int(len(testList) / 2)
        left = wonderSort(testList[:middle])
        right = wonderSort(testList[middle:])
        result = []
        print("Left: ", left)
        print("Right: ", right)

        while len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left.pop(0)
            else:
                result.append(right[0])
                right.pop(0)
            result += left
            result += right
            print("Result: ", result)
        return result

    print(wonderSort(testList))

    5.
    num = 10
    def addOnesToTestList(num):
        testList = []

        for i in range(0, num):
            testList.append(1)
            print(testList)
        return testList

    print(addOnesToTestList(num))

    6.
    list = [2,3,4,5,6,7,8,9,10,11]
    def search(num, lst):
        print(f" The list is {lst} ")
        pivot = len(lst)//2
        print(f" Pivot element : {pivot}")

        if num == lst[pivot]:
            return "Element found"
        elif num < lst[pivot]:
            lst = lst[:pivot]
            return search(num, lst)
        elif num > lst[pivot]:
            lst = lst[pivot:]
            return search(num, lst)

    print(search(11, list))

    ---
    7.
    num = 10
    def calc_sum(num):
        if num <= 0:
            return 0
        else:
            print(f" Calculating {num} + calc_sum({num-1})")

        return num + calc_sum(num-1)

    print(calc_sum(num))
---