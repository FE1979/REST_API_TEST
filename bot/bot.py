import requests
import json

base_url = 'http://localhost:8000/'
like = 'like/'
unlike = 'unlike/'
users = 'users/'
posts = 'posts/'
get_token = 'api/token/'

New_users = {
    'Mike': {'username': 'Mike', 'email': '', 'password': 'mikepassword'},
    'Ford': {'username': 'Ford', 'email': '', 'password': 'modelt'}
}


class User():
    """ User class """

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.auth = {'username': self.username, 'password': self.password}


    def sign_up(self):
        """ Sing up new user
            return:     requests.response
        """

        resp = requests.post(base_url + users, data=self.auth)
        return resp


    def get_token(self):
        """ Returns token for user """

        resp = requests.post(base_url + get_token, data=self.auth)
        tokens = json.loads(resp.text)
        token = tokens['access']

        return token


    def get_header(self):
        header = {"Content-Type": "application/json", "Authorization": "Bearer "
                   + self.get_token()}

        return header


    def create_post(self, post):
        """ Creates post by sending post request
            input_post: post with 'title' and 'body' desribed
            input_type: dict
            return:     requests.response
        """

        resp = requests.post(base_url + posts, headers=self.get_header(),
                             data=json.dumps(post))

        return resp


    def like_post(self, post_number):
        """ Likes post
            input:      post_number
            input_type: integer
            return:     requests.response
        """

        resp = requests.post(base_url + posts + f'{post_number}/' + like,
            headers=self.get_header())

        return resp


    def unlike_post(self, post_number):
        """ Unlikes post
            input:      post_number
            input_type: integer
            return:     requests.response
        """

        resp = requests.post(base_url + posts + f'{post_number}/' + unlike,
            headers=self.get_header())

        return resp

#create a Ford user
user_data = New_users['Ford']
ford = User(user_data['username'],user_data['email'], user_data['password'])

#Let create another post from Ford
post = {'title': 'Black car...',
        'body': 'I like black cars and black coffee. Time for coffee break! \
        (photo as usual)'}

print(ford.create_post(post))
print(ford.like_post(5))
print(ford.like_post(6))
print(ford.unlike_post(6))
