# ag_twitter_api: AG Twitter APIs 

### Description

The main job will be to develop two API endpoint that connects through the twitter API and expose two RESTful endpoints.

1. Get tweets by a hashtag: get the list of tweets with the given hashtag.
2. Get user tweets.​ Get the list of tweets that user has on his feed in json format.

### Installation

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
virtualenv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

Install packages into the virtualenv

```
cd twitter_api
pip install -r requirements.txt
```

### How to use
```
python manage.py runserver 127.0.0.1:8000 --settings=twitter_api.settings
```


### Document

[http://127.0.0.1:8000/docs/](http://127.0.0.1:8000/docs/)


