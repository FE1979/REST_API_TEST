# REST DJANGO API Demo
## Building simple social network on REST API

### Bot description:
Bot creates fake users with usernames, email and passwords to create and like posts randomly using REST API through requests python library.
It uses first_names.json and last_names.json to create users. Both files are plain lists.

Quotes.json is used to create posts and has simple format {"text": "author"}.
You can use your own content by changing settings in config.ini


### Quick look on config.ini:
General:      set up number of fake users and max posts and likes per user

API_settings: change it if server runs on other address

Content:      change content files


### Instalation procces.
Make directory for the project:
> mkdir <project_dir>

Run virtual environment into project directory:
> python3 -m venv <env_dir>
and activate it
> source bin/activate

Clone git repository into environment directory :
> git clone git@github.com:FE1979/REST_API_TEST.git

(or copy it to this directory if cloned before.)

Run instalation in REST_API_TEST directory:
> pip3 install -r requirenments.txt

> python3 manage.py migrate

> python3 manage.py createsuperuser **(Remember superuser login and password!)**

> python3 manage.py runserver

Now, you can run demo bot:
open new terminal and change directory to
> cd ../<project_dir>/<env_dir>

and activate virtual environment again
> source bin/activate

change directory to REST_API_TEST/bot and run:
> python3 main_bot.py


After that you can check the result of a bot on:
http://localhost:8000

Don't forget to use superuser credentials to view API on browser.



-------------------------------------------------------------------------------------------------
If tou have any ideas to improve this stuff
please contact me: ronin911@gmail.com
