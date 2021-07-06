# Dialogflow IVR Chatbot

## Demo Video
https://youtu.be/7k73qe_hLxM

## Drive Link 
https://drive.google.com/drive/folders/1hG3cqUPDleWUVGPYRZKyl659dPxZOc9s?usp=sharing

## Setup Instructions

### Download and run the app
The following sections guide you through configuring, running, and deploying the sample.

Clone the repository to your local machine:
```js 
git clone https://github.com/jeevana28/ivrchatbot.git
```
cd into the directory that contains the code/.
Alternatively, you can download the sample as a zip and extract it.

### Setting up your local environment
This is implemented in a local sqlite3 database 

### Build and run the app locally
To run the Django app on your local computer, you'll need to set up a Python development environment, including Python, pip, and virtualenv.

Create an isolated Python environment, and install dependencies:
```js
virtualenv env
env/Scripts/activate
pip install -r requirements.txt
```
Create an AppointmentScheduler.json file inside **chat** directory and paste the contents from the AppointmentScheduler.json file uploaded in the submitted zip file [link provided in ppt]

Run the Django migrations to add your models to database if in case they are not imported properly:
```js
python3 manage.py makemigrations
python3 manage.py migrate
```

***When appointement scheduler is called it sends a request to the concerned department regarding the meeting's time and date***
Please login from your google account with the following credentials 
email : ivrbot123@gmail.com
password : @Ivr1234
Activate access from less secure apps from this link 
https://www.google.com/settings/security/lesssecureapps


In test website only 1 IT department for testing
To check the email sent after appointment is scheduled you can login to the following account:
email : ivrtestit123@gmail.com
password : @bot1234

Start a local web server:
```js
python3 manage.py runserver
```
In your web browser, enter this address:

http://localhost:8000

You should see a homepage showing login and register options 
You can login with the following credentials:
    username = user1
    password = test4321
or 
Register with a new account and login 


You should see a simple webpage with the text: "Dialogflow" a text box and **submit** button. 

***To chat with chatbot please click on submit button after typing a message(not enter button)***
***To enable voice chat click on the start recording button on the right bottom of the screen***
***It works in english, fresh, dutch ***

The following order ids are added in database whose details can be checked :
Order id = 123456
Order id = 234567



The sample app pages are delivered by the Django web server running on your computer. When you're ready to move forward, press Ctrl+C to stop the local web server.

### Use the Django admin console
Create a superuser:
```js
python3 manage.py createsuperuser
```
Start a local web server:
```js
python3 manage.py runserver
```
Enter this address in your web browser. To log on to the admin site, use the username and password you created when you ran createsuperuser.

http://localhost:8000/admin/
