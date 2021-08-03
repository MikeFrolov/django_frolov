# Django_Frolov

### Hiilel Python Advanced course - Django

by Michail Frolov

---
### Use aplication with bash commands:

1. $pip3 install -r requirements.txt
2. $python3 manage.py migrate
3. $python3 manage.py createsuperuser -> enter username -> enter mail -> enter password -> re-enter password ->enter 'y'
4. $python3 manage.py runserve

To stop the server, press "ctrl + c"

---

Homework - 4:

    1. use "127.0.0.1:8000/generate-student/" address to generate 1 random student into the database
    2. use "127.0.0.1:8000/generate-students/?count=n" address to  generate n random students into the database,
       where n = number of objects to be generated
    3. use "127.0.0.1./admin/" address to manually create groups, students and teachers in the database
    4. use "127.0.0.1:8000/get_groups/" address to list all groups from the database
    5. use "127.0.0.1:8000/get_teachers/" address to list all teachers from the database


The minimum acceptable version of Python is 3.9

------

Read the task in file 'Tasks.txt'
