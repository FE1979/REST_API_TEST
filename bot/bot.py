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


def sign_up_user(user_creadentials):
    """ Sing up new user
        input_type: dict
        input:      username, email and password
        return:     requests.response
    """

    resp = requests.post(base_url + users, data=user_creadentials)
    return resp


def create_post(user, post):
    """ Creates post by sending post request
        input:      user
        input_post: post with 'title' and 'body' desribed
        input_type: dict
        return:     requests.response
    """
    auth = {'username': user['username'],
            'password': user['password']}

    # get token
    resp = requests.post(base_url + get_token, data=auth)
    tokens = json.loads(resp.text)
    token = tokens['access']

    # make post
    headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
    resp = requests.post(base_url + posts, headers=headers,
                         data=json.dumps(post))

    return resp


def like_post(user, post_number):
    """ Likes post
        input:      user
        input:      post_number
        input_type: integer
    """
    auth = {'username': user['username'],
            'password': user['password']}

    # get token
    resp = requests.post(base_url + get_token, data=auth)
    tokens = json.loads(resp.text)
    token = tokens['access']

    # make post
    headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
    resp = requests.post(
        base_url + posts + f'{post_number}/' + like,
        headers=headers
    )

    return resp


post = {'title': 'Morning post from Mike',
        'body': 'I had beacon on breakfast! (photo)'}

# let create a post from Mike
print(create_post(New_users['Mike'], post=post))

resp = requests.get(base_url + posts)
if resp.status_code == 200:
    posts_list = json.loads(resp.text)
    last_post = len(posts_list) - 1
else:
    print(resp)

# And Mike likes his morning post
print(like_post(New_users['Mike'], post_number=last_post))
