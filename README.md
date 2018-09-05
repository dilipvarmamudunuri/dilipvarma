
To Running the Project
 
1. Downlode the file from github
2. Open the terminal and change the directory up to where the manage.py file present
3. We need to create the database and change the database name in settings.py
4. To migrate the database use the commands below
	1.python3 manage.py makemigrations
	2.python3 manage.py migrate
5. We need to create the admin using the bellow commands
	1.python3 manage.py createsuperuser
6. To run the applications 
	python3 manage.py runserver
7. After running the application in url use the "uri" "localhost:8000/admin"
8. Use username and password to login 
9. Click the AddEmployee link and add employee fill the data and save
10. Remember the emailid and password to login the employee details use the url "localhost:8000/login"
11. It displays the all the employees and beside that there is a link "feadback" click on it and give the feedback submit u can check on admin page
