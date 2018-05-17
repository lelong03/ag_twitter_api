# ag_twitter_api: AG Twitter APIs 

### Description

The main job will be to develop two API endpoint that connects through the twitter API and expose two RESTful endpoints.

1. Get tweets by a hashtag: get the list of tweets with the given hashtag.
2. Get user tweets.​ Get the list of tweets that user has on his feed in json format.


### Installation

**This project needs to be run in python 3**

Install python 3 for Ubuntu & virtualenv:
```
apt-get install python3-pip
pip3 install virtualenv
```

Create folder that contains the project
```
mkdir <Path_To_Folder_Project>
cd <Path_To_Folder_Project>
```

Clone code from GITHUB
```
git clone https://github.com/lelong03/ag_twitter_api.git
cd ag_twitter_api
```

Create a virtualenv to isolate our package dependencies locally
```
python3 -m virtualenv env
source env/bin/activate  # On Windows use `env\Scripts\activate.bat`
```

Install packages into the virtualenv
```
cd twitter_api
pip install -r requirements.txt
```


### How to use

Run API services by command:
```
python manage.py runserver 127.0.0.1:8000 --settings=twitter_api.settings
```


Endpoints:


http://127.0.0.1:8000/hashtags/<hashtag_string>?pages_limit=<number_of_items>

| Param        | Description           |
| ------------- |-------------|
|   hashtag_string      | hash tag content that you would like to search tweets           |
|   number_of_items     | number of tweets that to retrieve           |


http://127.0.0.1:8000/user/<user_screen_name>?pages_limit=<number_of_items>

| Param        | Description           |
| ------------- |-------------|
|   user_screen_name    | screen name of user whom you would like to search tweets belong to          |
|   number_of_items     | number of tweets that to retrieve           |


**Note:** user screen name is different from the full name of user. This is the unique string that stays under the full name and starts with "@" in user profile page.


### Document

After service is run. Browse this link to see service document

[http://127.0.0.1:8000/docs/](http://127.0.0.1:8000/docs/)


### Unit-test
```
cd test
python tweet_test.py
```


