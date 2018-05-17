#!/usr/bin/env bash
# Clone code from GITHUB
git clone [url]
cd ag_twitter_api

# Create a virtualenv to isolate our package dependencies locally
virtualenv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install packages into the virtualenv
cd twitter_api
pip install -r requirements.txt

# Set up a new project with a single application
django-admin.py startproject twitter_api .  # Note the trailing '.' character
cd twitter_api