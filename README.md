# Django_Frolov

=======

### Hiilel Python Advanced course - Django

by Michail Frolov

---
### Use aplication with bash commands:

1. $pip3 install -r requirements.txt
2. $python3 manage.py migrate
3. $python3 manage.py createsuperuser -> enter username -> enter mail -> enter password -> re-enter password ->enter 'y'
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
The minimum acceptable version of Python is 3.9

---

(Read tasks in file 'Tasks.txt')
