# Django_Frolov
Python Advanced course - Django


### Use application with bash commands:

1. $pip3 install -r requirements.txt
2. $python3 manage.py migrate
3. $python3 manage.py createsuperuser -> enter username -> enter mail -> enter password -> re-enter password ->enter 'y'
4. $python3 manage.py runserver

######To stop the server, press "ctrl + c"

---

Homework - 4:

    1. use "127.0.0.1:8000/generate-student/" address to generate 1 random student into the database
    2. use "127.0.0.1:8000/generate-students/?count=n" address to  generate n random students into the database,
       where n = number of objects to be generated
    3. use "127.0.0.1./admin/" address to manually create groups, students and teachers in the database
    4. use "127.0.0.1:8000/get_groups/" address to list all groups from the database
    5. use "127.0.0.1:8000/get_teachers/" address to list all teachers from the database
 
Homework - 5:

    1. use bash command "flake8 Django_Frolov" to check the design of the code in the all project
    2. use bash command "python3 manage.py generate_teachers n" to  generate n random teachers into the database,
       where n = number of objects to be generated
    3. use "127.0.0.1:8000/get_teachers/?" address with "id=int", "first_name=str", "last_name=str", "age=int"
       parameters, to filter teachers by parameter. 
       Use & to combine 2 or more filtering parameters.
       Example: "127.0.0.1:8000/get_teachers/?first_name=Vitalii&age=30"

---
The minimum acceptable version of Python is 3.9

(Read tasks in file 'Tasks.txt')
