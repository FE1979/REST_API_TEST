import requests
import json


class User():
    """ User class """

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.auth = {'username': self.username, 'password': self.password}
        self.data = {'username': self.username, 'email': self.email,
                     'password': self.password}

    def sign_up(self, url):
        """ Sing up new user
            input:  sign up url
            return: requests.response
        """
        headers = {"Content-Type": "application/json"}
        resp = requests.post(url, headers=headers, data=json.dumps(self.data))
        return resp


    def get_tokens(self, url):
        """ Gets token for user
            input:  tokens url
            return: requests.response
        """

        resp = requests.post(url, data=self.auth)
        tokens = json.loads(resp.text)
        self.access_token = tokens['access']
        self.refresh_token = tokens['refresh']

        return resp


    def get_header(self):
        header = {"Content-Type": "application/json", "Authorization": "Bearer "
                   + self.access_token}

        return header


    def create_post(self, url, post):
        """ Creates post by sending post request
            input url:  posts url
            input post: post with 'title' and 'body' desribed
            input_type: dict
            return:     requests.response
        """

        resp = requests.post(url, headers=self.get_header(),
                             data=json.dumps(post))

        return resp


    def like_post(self, url, post_number):
        """ Likes post
            input url:  posts url
            input:      post_number
            input_type: integer
            return:     requests.response
        """

        resp = requests.post(url + f'{post_number}/like/',
            headers=self.get_header())

        return resp


    def unlike_post(self, url,  post_number):
        """ Unlikes post
            input url:  posts url
            input:      post_number
            input_type: integer
            return:     requests.response
        """

        resp = requests.post(url + f'{post_number}/unlike',
            headers=self.get_header())

        return resp
