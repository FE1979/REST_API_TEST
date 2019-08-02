import json
import requests
import configparser
from random import choice, random

from bot_users import User


# Load settings
config = configparser.ConfigParser()
config.read('config.ini')

# Get API settings
base_url = config.get('API_settings', 'base_url')
users_url = config.get('API_settings', 'users_url')
posts_url = config.get('API_settings', 'posts_url')
get_token_url = config.get('API_settings', 'get_token_url')

# Get content
first_names = []
with open(config.get('Content', 'first_names'), 'r') as f:
    first_names = json.loads(f.read())

last_names = []
with open(config.get('Content', 'last_names'), 'r') as f:
    last_names = json.loads(f.read())

quotes = []
with open(config.get('Content', 'quotes'), 'r') as f:
    quotes = json.loads(f.read())

# Get general settings
user_numbers = int(config.get('General', 'users_numbers'))
max_posts_per_user = int(config.get('General', 'max_posts_per_user'))
max_likes_per_user = int(config.get('General', 'max_likes_per_user'))


# RUN BOT

# Create users and get access token for each
i = 0
users_container = []
while i < user_numbers:

    # create fake name, email and password
    username = ''.join([choice(first_names), choice(last_names)])
    email = '@'.join([username, 'gmail.com'])
    password = ''.join([username, 'pswd'])
    new_user = User(username, email, password)

    # sign up in API and get token
    resp = new_user.sign_up(base_url + users_url)
    resp = new_user.get_tokens(base_url + get_token_url)

    # register new user in our container
    users_container.append(new_user)

    #next one
    i +=1


# Let every user make posts under max_posts_per_user

print('posting...')
for user in users_container:

    i = 0
    while i < max_posts_per_user:
        post = {'title': '', 'body': ''}
        # Let create a post from famous people quotes
        post['title'] = choice(quotes)['author']
        post['body'] = choice(quotes)['text']

        # use 80% chance to create a post
        resp = random() < 0.8 and  user.create_post(base_url + posts_url, post)
        print(resp)

        i += 1


# Let our users like other user's posts
for user in users_container:

    # get list of posts
    resp = requests.get(base_url + posts_url)
    print('Retrieve posts list')
    print(resp)
    posts_list = json.loads(resp.text)

    # set likes for user
    likes = [True for i in range(max_likes_per_user)]

    print('Liking...')
    for p in posts_list:
        if likes:
            if random() < 0.6:
                post_number = posts_list.index(p) + 1
                resp = user.like_post(base_url + posts_url, post_number)
                print(resp)
                # get out one like from user
                likes.pop()
