# Django_Frolov

=======

### Hiilel Python Advanced course - Django

by Michail Frolov

---
### Use aplication with bash commands:

    1. $source venv/bin/activate
    2. $pip3 install -r requirements.txt
    2. $python3 manage.py migrate
    3. $python3 manage.py createsuperuser -> enter username -> enter mail -> enter password ->
     -> re-enter password ->enter 'y'
    4. $python3 manage.py runserver

    *To stop the server, press "ctrl + c"
---
Homework - 4:

    1. use "127.0.0.1:8000/generate-student/" address to generate 1 random student into the database
    2. use "127.0.0.1:8000/generate-students/?count=n" address to  generate n random students into the database,
       where n = number of objects to be generated
    3. use "127.0.0.1./admin/" address to manually create groups, students and teachers in the database
    4. use "127.0.0.1:8000/get_groups/" address to list all groups from the database
    5. use "127.0.0.1:8000/get_teachers/" address to list all teachers from the database
---
Homework - 5:

    1. use bash command "flake8" to check the design of the code in the all project

    2. use bash command "python3 manage.py generate_teachers n" to  generate n random teachers into the database,
       where n = number of objects to be generated
    3. use "127.0.0.1:8000/list_teachers/" or "127.0.0.1:8000/list students/" addresses to list all teachers
       or stodents from database
    3. use "127.0.0.1:8000/list_teachers/?" or "127.0.0.1:8000/list_students/?" addresses with "id=int",
       "first_name=str", "last_name=str", "age=int" parameters, to list filtered teachers or students from database
       by parameter. 
       Use & to combine 2 or more filtering parameters.
       * Example: "127.0.0.1:8000/get_teachers/?first_name=Vitalii&age=30"
---
Homework - 6:

    1. use "127.0.0.1:8000/create_student_form/" address to create new student with use html form
    2. use "127.0.0.1:8000/create_teacher_form/" address to create new teacher with use html form
    3. use "127.0.0.1:8000/create_group_form/" address to create new group with use html form
---
Homework - 7:

    1. use "127.0.0.1:8000/list_objects/" address to list all objects. (objects - name of the 
        required class (students, teachers ...))
        - press 'edit' to edit object,
        - press 'delete' to delete object.
            *After creating, editing or deleting any object, the form will redirect to the page, 
            where the full list of objects of this class will be displayed.
    2. use "127.0.0.1:8000/admin/" address to go to the admin panel page with updated functionality:
        - all objects are displayed as a table,
        - added filtering by fields,
        - added search field for two main object fields, using (__startswith)
---
Homework - 8:

    1. Use "127.0.0.1:8000/create-student-form/ address to create new student with phone field,
            The phone number will not pass validation if:
            - it does not conform with the E-164 standard;
            - instead of numbers, you entered a letter or a sign other than ('', '-', '(', ')');
            - the number does not start with '+';
            - a country or city code that does not exist has been entered!
    2. In the form of creating a student and a teacher, fill in the first and last name in lower case,
        they will automatically be written to the base starting with a capital letter,
        implemented in signals / pre-save (handlers.py)
    3. Go to the address: http://127.0.0.1:8000/admin/general/logger/
        to view the activity log in the admin panel of the project
        implemented in .general/middleware.py
    4. copy.copy()- creates a shallow copy of the mutable object, while copy.deepcopy() - a full copy of it
---
Homework - 9:
    
    1. Travis CI connected to the project
        When sending a push to github, travis CI checks the project against the verification parameters specified
        in the travis.yml file.
    2. Configured RabbitMQ, Celery, Celery beat:
        2.1 Use next bash comands in new terminal to start Rabbitmq server:
            - cd /usr/local/Cellar/rabbitmq/3.9.5
            - brew services stop rabbitmq
            - sbin/rabbitmq-server
            If server is not work, use:
                - sudo lsof -i :25672
                - enter sistem password
                - sudo kill <PID>(when PID - Port id)
                - sbin/rabbitmq-server
        2.2 Use next bash comand in new terminal to start celery:
            - celery -A django_frolov worker -l INFO
            If not celery is not work, delete db.sqlite3 file and do it again
        2.3 Use next bash comand in new terminal to start celery beat:
            - celery -A django_frolov beat -l INFO
    3. Celery beat is configured to delete admin logs older than 7 days, task completion time: 12:00 every day
            - Use the previous instruction to start the Task Scheduler!
    4. Follow the link 'http://127.0.0.1:8000/contact_us/', fill out the form, click 'Save form':
        - In the root directory create a .env file with EMAIL_HOST_PASSWORD = ********
---
Homework - 10:

    1. Added foreign keys to the Group model for the curator (Teacher) and students (Student).
    2. Displayed groups with relationships to tables (admin / groups / group /) and (locall / list_groups /)
    3. Updated the script for generating random teachers:
        - 1 group with a random number of students (up to 10) is generated for each new teacher;
        - One of these students is randomly selected by the headman;
        - Use python manage.py generate_teachers n (where 'n' is the number of teachers);
    4. Created a new "currency" app:
        - Added 2 separate tasks for parsing the USD and EUR exchange rates from monobank and the national bank
            to the database;
        - Displayed the table of exchange rates from the database to the project page (use the link Exchange rates)
---
Homework - 11:

    1. Updated bootstrap to the version 5.1.
    2. Displayed currency/list_exchange_rates.html with bootstrap tables
    3. Updated the Travis CI:
        - Installed django_extensions, added python manage.py validate_templates in the .travis.yml file
        - Added python manage.py checkin in the .travis.yml file
        - Added python manage.py makemigrations --check --dry-run in the .travis.yml file
        - Added pip check in the .travis.yml file
---
Homework - 12:

    Answered all questions on all 7 tests
---
Homework - 15:

    Deployed the project on heroku:
        Launching the application after refactoring:
            Use bash commands:
                'git push heroku master'
                'heroku run python manage.py migrate'
                'heroku run python manage.py createsuperuser'
                'heroku open' - to open web site with working application

---
    The minimum acceptable version of Python is 3.9
---
    (Read tasks in file 'Tasks.txt')
---